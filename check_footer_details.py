import re

pages = ['index.html', 'faq.html', 'company-registration-matara.html', 'deed-lawyer-matara.html', 'notary-public-matara.html', '404.html']

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    m = re.search(r'<footer[^>]*>.*?</footer>', c, re.DOTALL)
    if m:
        print(f"=== {p} ===")
        print(m.group(0))
