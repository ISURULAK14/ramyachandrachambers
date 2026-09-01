const http = require('http');
const fs = require('fs');
const path = require('path');
const { exec, spawn } = require('child_process');

// 1. Start a simple static server
const server = http.createServer((req, res) => {
    let filePath = path.join(__dirname, req.url === '/' ? 'index.html' : req.url.split('?')[0]);
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

server.listen(8090, () => {
    console.log("Server listening on http://localhost:8090");

    // Launch edge with remote debugging
    const edgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe";
    const chromeProc = spawn(edgePath, [
        '--headless=new',
        '--remote-debugging-port=9222',
        '--disable-gpu',
        'http://localhost:8090'
    ]);

    setTimeout(async () => {
        try {
            // Fetch list of targets from CDP
            const targetsRes = await fetch('http://localhost:9222/json');
            const targets = await targetsRes.json();
            console.log("CDP Targets:", targets.length);
            const pageTarget = targets.find(t => t.type === 'page');
            if (pageTarget && pageTarget.webSocketDebuggerUrl) {
                console.log("Found page WS URL:", pageTarget.webSocketDebuggerUrl);
                const WebSocket = require('ws');
                // If ws not installed, we can also use CDP HTTP endpoints
            }
        } catch (e) {
            console.log("CDP fetch err:", e.message);
        }
        chromeProc.kill();
        server.close();
    }, 3000);
});
