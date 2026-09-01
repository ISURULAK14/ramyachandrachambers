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

server.listen(8096, async () => {
    const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });

    await page.goto('http://localhost:8096/index.html', { waitUntil: 'networkidle0' });

    // 1. Check Review Boxes portrait layout and dimensions
    const reviewStats = await page.evaluate(() => {
        const r1 = document.querySelector('.review-card-google');
        const r2 = document.querySelector('.review-card-direct');
        return {
            card1: r1 ? { width: r1.getBoundingClientRect().width, height: r1.getBoundingClientRect().height } : null,
            card2: r2 ? { width: r2.getBoundingClientRect().width, height: r2.getBoundingClientRect().height } : null,
        };
    });
    console.log("Review Box Portrait Dimensions:", reviewStats);

    // 2. Test Mouse Cursor Animation
    await page.mouse.move(500, 400);
    await new Promise(r => setTimeout(r, 200));

    const cursorActive = await page.evaluate(() => {
        const field = document.querySelector('.cursor-pixel-field');
        return {
            hasReadyClass: document.body.classList.contains('pixel-cursor-ready'),
            fieldTransform: field ? field.style.transform : null,
            fieldOpacity: field ? window.getComputedStyle(field).opacity : null
        };
    });
    console.log("Cursor Animation State:", cursorActive);

    // 3. Screenshot Testimonials Section
    const testSec = await page.$('#testimonials');
    if (testSec) {
        await testSec.screenshot({ path: 'portrait_reviews_audit.png' });
        console.log("Saved portrait_reviews_audit.png");
    }

    // 4. Screenshot Contact Section (Office boxes) for side-by-side comparison
    const contactSec = await page.$('#contact');
    if (contactSec) {
        await contactSec.screenshot({ path: 'office_boxes_comparison.png' });
        console.log("Saved office_boxes_comparison.png");
    }

    await browser.close();
    server.close();
    process.exit(0);
});
