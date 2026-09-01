import subprocess
import os
from PIL import Image

# Let's extract 0ed49c3 index.html
res = subprocess.run(['git', 'show', '0ed49c3:index.html'], capture_output=True, text=True)
with open('orig_index.html', 'w', encoding='utf-8') as f:
    f.write(res.stdout)

# Take screenshot of orig_index.html with orig_style.css
out_orig = os.path.abspath("test_orig_index.png")
cmd = f'"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" --headless --disable-gpu --screenshot="{out_orig}" --window-size=1280,3500 "file:///{os.path.abspath("orig_index.html")}"'
subprocess.run(cmd, shell=True)

if os.path.exists(out_orig):
    img = Image.open(out_orig)
    w, h = img.size
    print(f"Captured 0ed49c3 index: {w} x {h}")
    for i in range(3):
        t, b = i * 1100, min(h, (i + 1) * 1100)
        img.crop((0, t, w, b)).save(f'orig_slice_{i+1}.png')
        print(f"Saved orig_slice_{i+1}.png")
