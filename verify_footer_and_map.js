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

server.listen(8092, async () => {
    const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });

    await page.goto('http://localhost:8092/index.html', { waitUntil: 'networkidle0' });

    // 1. Screenshot World Map before any pins light up / during sequence
    const mapWrapper = await page.$('.map-wrapper');
    if (mapWrapper) {
        await new Promise(r => setTimeout(r, 600)); // 2 pins active (USA + UK)
        await mapWrapper.screenshot({ path: 'map_0_transparency_step2.png' });
        console.log("Saved map_0_transparency_step2.png");
    }

    // 2. Screenshot Footer
    const footer = await page.$('footer.site-footer');
    if (footer) {
        await footer.screenshot({ path: 'footer_clean.png' });
        console.log("Saved footer_clean.png");
    }

    // Check footer links text
    const footerLinks = await page.evaluate(() => {
        const links = [...document.querySelectorAll('footer a')];
        return links.map(a => a.textContent.trim());
    });
    console.log("Footer links found in DOM:", footerLinks);

    await browser.close();
    server.close();
    process.exit(0);
});
