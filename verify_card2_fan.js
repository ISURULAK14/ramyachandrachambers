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

server.listen(8098, async () => {
    const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });

    await page.goto('http://localhost:8098/index.html', { waitUntil: 'networkidle0' });

    const card2 = await page.$('.office-card-2');
    if (card2) {
        // Screenshot default card 2
        await card2.screenshot({ path: 'card2_default_stack.png' });

        // Hover card 2 to trigger Apple fan out
        await card2.hover();
        await new Promise(r => setTimeout(r, 600));
        await card2.screenshot({ path: 'card2_hover_fanned.png' });
        console.log("Saved card2_hover_fanned.png");
    }

    await browser.close();
    server.close();
    process.exit(0);
});
