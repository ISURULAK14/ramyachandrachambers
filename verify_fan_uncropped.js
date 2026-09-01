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

server.listen(8090, async () => {
    const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });

    await page.goto('http://localhost:8090/index.html', { waitUntil: 'networkidle0' });

    // Measure Fort & Kotavila photo dimensions
    const dimensions = await page.evaluate(() => {
        const fort = document.querySelector('.fort-gallery');
        const kota = document.querySelector('.kotavila-gallery');
        return {
            fort: fort ? { width: fort.getBoundingClientRect().width, height: fort.getBoundingClientRect().height } : null,
            kota: kota ? { width: kota.getBoundingClientRect().width, height: kota.getBoundingClientRect().height } : null
        };
    });
    console.log("Office Photo Dimensions (+20%):", dimensions);

    // Capture unhovered contact section
    const contactSec = await page.$('#contact');
    if (contactSec) {
        await contactSec.screenshot({ path: 'offices_20pct_larger.png' });
        console.log("Saved offices_20pct_larger.png");
    }

    // Hover Card 2 and capture full fanned-out view
    const card2 = await page.$('.office-card-2');
    if (card2) {
        await card2.hover();
        await new Promise(r => setTimeout(r, 600));
        await card2.screenshot({ path: 'card2_fanned_uncropped.png' });
        console.log("Saved card2_fanned_uncropped.png");
    }

    await browser.close();
    server.close();
    process.exit(0);
});
