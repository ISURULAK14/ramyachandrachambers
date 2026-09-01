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

    // ================= MOBILE VIEWPORT (iPhone 375x812) =================
    await page.setViewport({ width: 375, height: 812, isMobile: true, hasTouch: true });
    await page.goto('http://localhost:8099/index.html', { waitUntil: 'networkidle0' });

    // 1. Verify Canvas & Ambient Animation on Mobile
    const bgStatus = await page.evaluate(() => {
        const canvas = document.getElementById('ambient-cosmos-canvas');
        const ambient = document.querySelector('.global-ambient-system');
        const blobs = [...document.querySelectorAll('.ambient-layer')];
        return {
            canvasExists: !!canvas,
            canvasDisplay: canvas ? window.getComputedStyle(canvas).display : 'none',
            canvasOpacity: canvas ? window.getComputedStyle(canvas).opacity : '0',
            canvasWidth: canvas ? canvas.width : 0,
            canvasHeight: canvas ? canvas.height : 0,
            ambientDisplay: ambient ? window.getComputedStyle(ambient).display : 'none',
            blobsCount: blobs.length,
            blobAnimations: blobs.map(b => window.getComputedStyle(b).animationName)
        };
    });
    console.log("Mobile Background Animation Status:", bgStatus);

    // 2. Check Mobile Scroll Overflow
    const overflowCheck = await page.evaluate(() => {
        return {
            scrollWidth: document.body.scrollWidth,
            innerWidth: window.innerWidth,
            hasSpill: document.body.scrollWidth > window.innerWidth
        };
    });
    console.log("Mobile Scroll Overflow Check:", overflowCheck);

    // 3. Screenshot Hero on Mobile with Ambient BG
    await page.screenshot({ path: 'mobile_hero_ambient_bg.png' });
    console.log("Saved mobile_hero_ambient_bg.png");

    // 4. Scroll to Testimonials and capture
    await page.evaluate(() => {
        document.getElementById('testimonials').scrollIntoView();
    });
    await new Promise(r => setTimeout(r, 600));
    const testSec = await page.$('#testimonials');
    if (testSec) {
        await testSec.screenshot({ path: 'mobile_testimonials_section.png' });
        console.log("Saved mobile_testimonials_section.png");
    }

    // 5. Scroll to Contact and capture
    await page.evaluate(() => {
        document.getElementById('contact').scrollIntoView();
    });
    await new Promise(r => setTimeout(r, 600));
    const contactSec = await page.$('#contact');
    if (contactSec) {
        await contactSec.screenshot({ path: 'mobile_contact_section.png' });
        console.log("Saved mobile_contact_section.png");
    }

    await browser.close();
    server.close();
    process.exit(0);
});
