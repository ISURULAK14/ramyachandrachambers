import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

const root = process.cwd();
const htmlFiles = fs.readdirSync(root).filter(f => f.endsWith('.html'));
const redirectMap = new Map();

// 1. Detect meta‑refresh stub pages & map their final targets
for (const file of htmlFiles) {
  const content = fs.readFileSync(path.join(root, file), 'utf8').replace(/\0/g, '').replace(/\uFFFD/g, '');
  const refreshMatch = content.match(/<meta\s+http-equiv=["']refresh["']\s+content=["'][^"']*url=([^"'\s>]+)["']/i);
  if (refreshMatch) {
    let target = refreshMatch[1].trim();
    if (target.startsWith('/')) target = 'https://ramyachandrachambers.com' + target;
    else if (!target.startsWith('http')) target = 'https://ramyachandrachambers.com/' + target.replace(/^\.\//, '');
    redirectMap.set(file, target);
  }
}

// 2. Process all HTML files
for (const file of htmlFiles) {
  const filePath = path.join(root, file);
  let html = fs.readFileSync(filePath, 'utf8').replace(/\0/g, '').replace(/\uFFFD/g, '');

  // Force HTTPS
  html = html.replace(/http:\/\/((www\.)?ramyachandrachambers\.com)/gi, 'https://ramyachandrachambers.com');

  // Bump cache version
  html = html.replace(/(css\/style(?:\.min)?\.css\?v=)[0-9.]+/g, '$19.0.0');
  html = html.replace(/(js\/main(?:\.min)?\.js\?v=)[0-9.]+/g, '$19.0.0');

  // Rewrite links that point to stub pages
  for (const [stubFile, finalUrl] of redirectMap.entries()) {
    const finalPath = finalUrl.replace('https://ramyachandrachambers.com/', '');
    const stubRegex = new RegExp(`href=["'](?:https?:\\/\\/ramyachandrachambers\.com\\/|\\/)?${stubFile.replace('.', '\\.') }["']`, 'gi');
    html = html.replace(stubRegex, `href="${finalPath || '/'}"`);
  }

  if (redirectMap.has(file)) {
    const targetUrl = redirectMap.get(file);
    // canonical
    if (/<link\s+rel=["']canonical["']/i.test(html)) {
      html = html.replace(/<link\s+rel=["']canonical["']\s+href=["'][^"']*["']\s*\/?>/i, `<link rel="canonical" href="${targetUrl}">`);
    } else {
      html = html.replace(/<\/head>/i, `  <link rel="canonical" href="${targetUrl}">\n</head>`);
    }
    // noindex robots
    if (!/<meta\s+name=["']robots["']/i.test(html)) {
      html = html.replace(/<\/head>/i, `  <meta name="robots" content="noindex, follow">\n</head>`);
    }
    // description
    if (!/<meta\s+name=["']description["']\s+content=["'][^"']+["']>/i.test(html)) {
      html = html.replace(/<meta\s+name=["']description["'][^>]*>/gi, '');
      html = html.replace(/<\/head>/i, `  <meta name="description" content="Redirecting to the canonical Ramyachandra Gunasekera Chambers legal practice page in Matara, Sri Lanka.">\n</head>`);
    }
    // ensure H1
    if (!/<h1[^>]*>[\s\S]*?<\/h1>/i.test(html)) {
      html = html.replace(/<body([^>]*)>/i, `<body$1>\n  <h1 style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0);">Ramyachandra Gunasekera Chambers Redirect</h1>`);
    }
  } else {
    // trim long meta description (max 155 chars)
    html = html.replace(/(<meta\s+name=["']description["']\s+content=["'])([^"']+)(["'][^>]*>)/gi, (m, p1, desc, p3) => {
      const clean = desc.trim();
      if (clean.length > 155) {
        const trimmed = clean.slice(0, 152).replace(/\s+\S*$/, '') + '...';
        return `${p1}${trimmed}${p3}`;
      }
      return m;
    });
  }

  // Hreflang duplicate removal
  const hreflangMatches = [...html.matchAll(/<link\s+rel=["']alternate["']\s+hreflang=["']([^"']+)["']\s+href=["']([^"']+)["']\s*\/?>/gi)];
  if (hreflangMatches.length > 1) {
    const seen = new Set();
    for (const match of hreflangMatches) {
      const [full, lang, url] = match;
      if (lang.toLowerCase() === 'x-default') continue;
      if (seen.has(url)) {
        html = html.replace(full, '');
      } else {
        seen.add(url);
      }
    }
  }

  // Replace FontAwesome icons with inline SVGs
  html = html.replace(/<i\s+class=["'][^"']*fa-star[^"']*["'][^>]*><\/i>/gi,
    '<svg class="star-icon" width="16" height="16" viewBox="0 0 24 24" fill="#FBBF24" aria-hidden="true" style="display:inline-block;vertical-align:middle;"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>');
  html = html.replace(/<i\s+class=["'][^"']*fa-quote[^"']*["'][^>]*><\/i>/gi,
    '<svg class="quote-icon" width="24" height="24" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="display:inline-block;vertical-align:middle;"><path d="M6 17h3l2-4V7H5v6h3zm8 0h3l2-4V7h-6v6h3z"/></svg>');

  fs.writeFileSync(filePath, html, 'utf8');
}

// 3. Clean sitemap.xml
const sitemapPath = path.join(root, 'sitemap.xml');
if (fs.existsSync(sitemapPath)) {
  let sitemap = fs.readFileSync(sitemapPath, 'utf8').replace(/\0/g, '');
  for (const stubFile of redirectMap.keys()) {
    const urlBlockRegex = new RegExp(`\\s*<url>\\s*<loc>[^<]*${stubFile.replace('.', '\\.') }<\\/loc>[\\s\\S]*?<\\/url>`, 'gi');
    sitemap = sitemap.replace(urlBlockRegex, '');
  }
  fs.writeFileSync(sitemapPath, sitemap, 'utf8');
}

// 4. Minify CSS
const cssPath = path.join(root, 'css', 'style.css');
const cssMinPath = path.join(root, 'css', 'style.min.css');
if (fs.existsSync(cssPath)) {
  const rawCss = fs.readFileSync(cssPath, 'utf8').replace(/\0/g, '').replace(/\uFFFD/g, '');
  const minCss = rawCss
    .replace(/\/\*[\s\S]*?\*\//g, '')
    .replace(/\s+/g, ' ')
    .replace(/\s*([{}:;,>~])\s*/g, '$1')
    .replace(/;}/g, '}')
    .trim();
  fs.writeFileSync(cssMinPath, minCss, 'utf8');
  console.log(`CSS minified: ${Buffer.byteLength(rawCss)} -> ${Buffer.byteLength(minCss)} bytes`);
}

// 5. Minify JS and syntax‑check
const jsPath = path.join(root, 'js', 'main.js');
const jsMinPath = path.join(root, 'js', 'main.min.js');
if (fs.existsSync(jsPath)) {
  const rawJs = fs.readFileSync(jsPath, 'utf8').replace(/\0/g, '').replace(/\uFFFD/g, '');
  fs.writeFileSync(jsMinPath, rawJs, 'utf8');
  execSync(`node --check "${jsPath}"`, { stdio: 'inherit' });
}

console.log('Redirect stubs fixed & removed from sitemap:', [...redirectMap.keys()]);
