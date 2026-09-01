import subprocess
import os
from PIL import Image

sections = ['services', 'practice-areas', 'testimonials', 'contact']

with open('index.html', 'r', encoding='utf-8') as f:
    orig_html = f.read()

for sec in sections:
    # Inject a tiny script at the end of head to scroll instantly to sec
    scroll_js = f'<script>window.addEventListener("DOMContentLoaded", () => {{ const el = document.getElementById("{sec}"); if(el) el.scrollIntoView(); }});</script>'
    temp_html = orig_html.replace('</head>', f'{scroll_js}</head>')
    
    with open('temp_scroll.html', 'w', encoding='utf-8') as f:
        f.write(temp_html)
    
    out = os.path.abspath(f"real_view_{sec}.png")
    cmd = f'"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" --headless --disable-gpu --screenshot="{out}" --window-size=1280,1000 "file:///{os.path.abspath("temp_scroll.html")}"'
    subprocess.run(cmd, shell=True)
    print(f"Captured real_view_{sec}.png (size: {os.path.getsize(out)} bytes)")
