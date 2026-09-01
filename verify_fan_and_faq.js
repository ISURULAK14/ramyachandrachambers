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

server.listen(8097, async () => {
    const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });

    // 1. Check Kotavila Gallery Default State
    await page.goto('http://localhost:8097/index.html', { waitUntil: 'networkidle0' });
    const kotavilaGal = await page.$('.kotavila-gallery');
    if (kotavilaGal) {
        await kotavilaGal.screenshot({ path: 'kotavila_default_stack.png' });
        console.log("Saved kotavila_default_stack.png");

        // Hover to trigger Apple-style fan out
        await kotavilaGal.hover();
        await new Promise(r => setTimeout(r, 600));
        await kotavilaGal.screenshot({ path: 'kotavila_fanned_out_apple.png' });
        console.log("Saved kotavila_fanned_out_apple.png");
    }

    // 2. Check FAQ Open / Close on faq.html
    await page.goto('http://localhost:8097/faq.html', { waitUntil: 'networkidle0' });
    const firstFaqHeader = await page.$('.faq-card .faq-header');
    if (firstFaqHeader) {
        // Click to open
        await firstFaqHeader.click();
        await new Promise(r => setTimeout(r, 900)); // wait for slow smooth transition
        await page.screenshot({ path: 'faq_opened_smooth.png' });
        console.log("Saved faq_opened_smooth.png");

        // Click to close
        await firstFaqHeader.click();
        await new Promise(r => setTimeout(r, 900));
        await page.screenshot({ path: 'faq_closed_smooth.png' });
        console.log("Saved faq_closed_smooth.png");
    }

    await browser.close();
    server.close();
    process.exit(0);
});
