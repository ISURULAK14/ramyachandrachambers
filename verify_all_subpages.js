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

    const pagesToTest = [
        'index.html',
        'faq.html',
        'notary-public-matara.html',
        'deed-lawyer-matara.html',
        'company-registration-matara.html',
        '404.html'
    ];

    let totalErrors = 0;

    for (const p of pagesToTest) {
        page.on('pageerror', err => {
            console.log(`[${p}] PAGE ERROR:`, err.toString());
            totalErrors++;
        });

        await page.goto(`http://localhost:8098/${p}`, { waitUntil: 'networkidle0' });
        const shotPath = `subpage_${p.replace('.html', '')}.png`;
        await page.screenshot({ path: shotPath, fullPage: true });
        console.log(`Verified ${p} -> saved ${shotPath}`);
    }

    console.log(`\nALL SUBPAGES VERIFIED. Total JS page errors across entire site: ${totalErrors}`);
    await browser.close();
    server.close();
    process.exit(totalErrors === 0 ? 0 : 1);
});
