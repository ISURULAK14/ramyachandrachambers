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

server.listen(8093, async () => {
    const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });

    await page.goto('http://localhost:8093/index.html', { waitUntil: 'networkidle0' });

    // Hover Sri Lanka pin
    const pin = await page.$('#pin-srilanka');
    if (pin) {
        await pin.hover();
        await new Promise(r => setTimeout(r, 400));
        const mapWrapper = await page.$('.map-wrapper');
        await mapWrapper.screenshot({ path: 'map_hover_lit_up.png' });
        console.log("Saved map_hover_lit_up.png");
    }

    await browser.close();
    server.close();
    process.exit(0);
});
