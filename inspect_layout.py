import subprocess
import os

js_eval = """
const puppeteer = require('puppeteer');
(async () => {
    //
})();
"""

# Let's inspect heights with Edge console logging
eval_script = """
window.addEventListener('load', () => {
    const sections = ['home', 'about', 'services', 'practice-areas', 'testimonials', 'contact'];
    sections.forEach(id => {
        const el = document.getElementById(id);
        if (el) {
            const rect = el.getBoundingClientRect();
            console.log(`SECTION #${id}: top=${rect.top + window.scrollY}, height=${rect.height}, offsetTop=${el.offsetTop}`);
        } else {
            console.log(`SECTION #${id}: NOT FOUND`);
        }
    });
});
"""

with open('inspect_dom.js', 'w', encoding='utf-8') as f:
    f.write(eval_script)

print("Created inspect_dom.js")
