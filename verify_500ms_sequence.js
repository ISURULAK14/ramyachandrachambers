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

server.listen(8099, async () => {
    const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });

    await page.goto('http://localhost:8099/index.html', { waitUntil: 'networkidle0' });

    const mapWrapper = await page.$('.map-wrapper');
    if (!mapWrapper) {
        console.log("Error: .map-wrapper not found");
        await browser.close();
        server.close();
        process.exit(1);
    }

    // Capture sequence 1 at 2100ms when all 5 countries in Sequence 1 are active
    await new Promise(r => setTimeout(r, 2100));
    await mapWrapper.screenshot({ path: 'seq_step_5_all5_active.png' });
    console.log("Saved seq_step_5_all5_active.png (Sequence 1: USA, UK, Sweden, Romania, Japan)");

    // Capture sequence 2 at 5100ms when all 5 countries in Sequence 2 are active
    await new Promise(r => setTimeout(r, 3000));
    await mapWrapper.screenshot({ path: 'seq_step_seq2_all5_active.png' });
    console.log("Saved seq_step_seq2_all5_active.png (Sequence 2: Portugal, Germany, UAE, Korea, Australia)");

    // Capture sequence 3 at 8100ms (Sequence 3: Norway, Luxembourg, Greece, Sri Lanka, China)
    await new Promise(r => setTimeout(r, 3000));
    await mapWrapper.screenshot({ path: 'seq_step_seq3_all5_active.png' });
    console.log("Saved seq_step_seq3_all5_active.png (Sequence 3: Norway, Luxembourg, Greece, Sri Lanka, China)");

    await browser.close();
    server.close();
    process.exit(0);
});
