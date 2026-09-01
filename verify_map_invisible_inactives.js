const puppeteer = require('puppeteer');
const http = require('http');
const fs = require('fs');
const path = require('path');

const server = http.createServer((req, res) => {
    let reqPath = req.url.split('?')[0];
    let filePath = path.join(__dirname, reqPath === '/' ? 'index.html' : reqPath);
    fs.readFile(filePath, (err, data) => {
        if (err) { res.writeHead(404); res.end("Not found"); return; }
        let ext = path.extname(filePath);
        let mime = {
            '.html': 'text/html', '.css': 'text/css', '.js': 'application/javascript',
            '.svg': 'image/svg+xml', '.png': 'image/png', '.gif': 'image/gif', '.webp': 'image/webp'
        }[ext] || 'text/plain';
        res.writeHead(200, { 'Content-Type': mime });
        res.end(data);
    });
});

server.listen(8094, async () => {
    const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });

    await page.goto('http://localhost:8094/index.html', { waitUntil: 'networkidle0' });

    // Check computed styles of inactive pins vs active pin
    const pinStats = await page.evaluate(() => {
        const allPins = [...document.querySelectorAll('.map-pin')];
        const inactivePins = allPins.filter(p => !p.classList.contains('active'));
        const activePins = allPins.filter(p => p.classList.contains('active'));

        const inactiveOpacities = inactivePins.map(p => window.getComputedStyle(p).opacity);
        const inactiveVisibilities = inactivePins.map(p => window.getComputedStyle(p).visibility);

        return {
            total: allPins.length,
            inactiveCount: inactivePins.length,
            activeCount: activePins.length,
            sampleInactiveOpacity: inactiveOpacities[0],
            sampleInactiveVisibility: inactiveVisibilities[0]
        };
    });

    console.log("Pin Invisibility Verification:", pinStats);

    const mapWrapper = await page.$('.map-wrapper');
    if (mapWrapper) {
        // Screenshot at 1100ms (3 pins active, 32 pins 100% invisible)
        await new Promise(r => setTimeout(r, 1100));
        await mapWrapper.screenshot({ path: 'map_strict_inactives_hidden.png' });
        console.log("Saved map_strict_inactives_hidden.png");
    }

    const contactSec = await page.$('#contact');
    if (contactSec) {
        await contactSec.screenshot({ path: 'contact_compact_boxes.png' });
        console.log("Saved contact_compact_boxes.png");
    }

    await browser.close();
    server.close();
    process.exit(0);
});
