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

server.listen(8095, async () => {
    const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
    const page = await browser.newPage();

    // ================= DESKTOP AUDIT (1280x900) =================
    await page.setViewport({ width: 1280, height: 900 });
    await page.goto('http://localhost:8095/index.html', { waitUntil: 'networkidle0' });

    const desktopHeights = await page.evaluate(() => {
        const c1 = document.querySelector('.office-card-1');
        const c2 = document.querySelector('.office-card-2');
        return {
            card1Height: c1 ? c1.getBoundingClientRect().height : 0,
            card2Height: c2 ? c2.getBoundingClientRect().height : 0
        };
    });
    console.log("Desktop Office Card Heights (px):", desktopHeights);

    const desktopNav = await page.$('.site-nav');
    if (desktopNav) await desktopNav.screenshot({ path: 'desktop_liquid_nav.png' });

    const desktopContact = await page.$('#contact');
    if (desktopContact) await desktopContact.screenshot({ path: 'desktop_equal_offices.png' });

    const desktopReviews = await page.$('#testimonials');
    if (desktopReviews) await desktopReviews.screenshot({ path: 'desktop_reviews_kept.png' });

    const desktopFooter = await page.$('.site-footer');
    if (desktopFooter) await desktopFooter.screenshot({ path: 'desktop_liquid_footer.png' });

    // ================= MOBILE AUDIT (375x812 - iPhone) =================
    await page.setViewport({ width: 375, height: 812, isMobile: true, hasTouch: true });
    await page.goto('http://localhost:8095/index.html', { waitUntil: 'networkidle0' });

    const mobileOverflow = await page.evaluate(() => {
        return {
            bodyScrollWidth: document.body.scrollWidth,
            windowInnerWidth: window.innerWidth,
            hasOverflow: document.body.scrollWidth > window.innerWidth
        };
    });
    console.log("Mobile Overflow Check:", mobileOverflow);

    await page.screenshot({ path: 'mobile_full_page.png', fullPage: true });
    console.log("Saved mobile_full_page.png");

    await browser.close();
    server.close();
    process.exit(0);
});
