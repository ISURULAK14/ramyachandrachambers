with open('orig_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
# Let's find every section tag in html
sections = re.findall(r'<section[^>]*id="([^"]+)"[^>]*>', html)
print("Sections in orig_index.html:", sections)

for s in sections:
    match = re.search(r'<section[^>]*id="' + s + r'"[^>]*>(.*?)</section>', html, re.DOTALL)
    if match:
        body = match.group(1).strip()
        print(f"\nSection #{s} (length: {len(body)} chars):")
        print(body[:200].replace('\n', ' '))
