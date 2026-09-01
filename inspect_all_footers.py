import glob
import re

html_files = glob.glob('*.html')
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.findall(r'<footer[^>]*>.*?</footer>', content, re.DOTALL)
    print(f"File: {fpath}, Footers found: {len(m)}")
