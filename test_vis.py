import subprocess
import os
from PIL import Image

# 1. First, fix the opacity: 0 bug in css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make .reveal visible by default so content is NEVER hidden!
css = css.replace('.reveal{opacity:0;transform:translateY(30px)', '.reveal{opacity:1;transform:none')
css = css.replace('.reveal{opacity:0;', '.reveal{opacity:1;')

# Ensure .map-wrapper and .map-bg-img are clean and not duplicating
# In .map-wrapper: remove background url if using <img>, or clean up <img>
css = css.replace('.map-bg-img{position:absolute;top:0;left:0;width:100%;height:100%;object-fit:fill;z-index:1;pointer-events:none;opacity:0.85;mix-blend-mode:screen}',
                  '.map-bg-img{position:absolute;top:0;left:0;width:100%;height:100%;object-fit:fill;z-index:1;pointer-events:none;opacity:0.75}')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated css/style.css: .reveal is now 100% visible by default!")

# 2. Take screenshots of faq.html and index.html
out_faq = os.path.abspath("test_visible_faq.png")
out_index = os.path.abspath("test_visible_index.png")

cmd_faq = f'"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" --headless --disable-gpu --screenshot="{out_faq}" --window-size=1280,1800 "file:///{os.path.abspath("faq.html")}"'
cmd_index = f'"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" --headless --disable-gpu --screenshot="{out_index}" --window-size=1280,4500 "file:///{os.path.abspath("index.html")}"'

subprocess.run(cmd_faq, shell=True)
subprocess.run(cmd_index, shell=True)

if os.path.exists(out_faq):
    print("FAQ screenshot captured:", out_faq)

if os.path.exists(out_index):
    img = Image.open(out_index)
    w, h = img.size
    print("Index screenshot size:", w, h)
    # Slices
    for i in range(4):
        t, b = i * 1100, min(h, (i + 1) * 1100)
        img.crop((0, t, w, b)).save(f'check_slice_{i+1}.png')
        print(f"Saved check_slice_{i+1}.png")
