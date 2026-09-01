const puppeteer = require('puppeteer');
const http = require('http');
const fs = require('fs');
const path = require('path');

const server = http.createServer((req, res) => {
    let reqPath = req.url.split('?')[0];
    let filePath = path.join(__dirname, reqPath === '/' ? 'index.html' : reqPath);
    fs.readFile(filePath, (err, data) => {
        if (err) {
            res.writeHead(404);
            res.end("Not found");
            return;
        }
        let ext = path.extname(filePath);
        let mime = {
            '.html': 'text/html',
            '.css': 'text/css',
            '.js': 'application/javascript',
            '.svg': 'image/svg+xml',
            '.png': 'image/png',
            '.gif': 'image/gif',
            '.webp': 'image/webp'
        }[ext] || 'text/plain';
        res.writeHead(200, { 'Content-Type': mime });
        res.end(data);
    });
});

server.listen(8095, async () => {
    console.log("Static server running on http://localhost:8095");
    const browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });

    const errors = [];
    page.on('console', msg => console.log('PAGE LOG:', msg.text()));
    page.on('pageerror', err => errors.push(err.toString()));

    // 1. Check FAQ Page
    console.log("Loading FAQ page...");
    await page.goto('http://localhost:8095/faq.html', { waitUntil: 'networkidle0' });
    await page.screenshot({ path: 'puppeteer_faq.png', fullPage: true });
    console.log("Saved puppeteer_faq.png");

    // Click first FAQ item
    const firstFaq = await page.$('.faq-header');
    if (firstFaq) {
        await firstFaq.click();
        await new Promise(r => setTimeout(r, 600));
        await page.screenshot({ path: 'puppeteer_faq_opened.png', fullPage: false });
        console.log("Saved puppeteer_faq_opened.png");
    }

    // 2. Check Index Page & World Map
    console.log("Loading Index page...");
    await page.goto('http://localhost:8095/index.html', { waitUntil: 'networkidle0' });
    await page.screenshot({ path: 'puppeteer_index_full.png', fullPage: true });
    console.log("Saved puppeteer_index_full.png");

    // Screenshot just the World Map element
    const mapWrapper = await page.$('.map-wrapper');
    if (mapWrapper) {
        await mapWrapper.screenshot({ path: 'puppeteer_map_element.png' });
        console.log("Saved puppeteer_map_element.png");
    }

    // Screenshot Services section
    const servicesSec = await page.$('#services');
    if (servicesSec) {
        await servicesSec.screenshot({ path: 'puppeteer_services.png' });
        console.log("Saved puppeteer_services.png");
    }

    console.log("Browser errors found:", errors.length);
    if (errors.length) console.log(errors);

    await browser.close();
    server.close();
    process.exit(0);
});
