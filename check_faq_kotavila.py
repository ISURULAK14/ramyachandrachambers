with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
print("=== FAQ CSS RULES ===")
for r in re.findall(r'(\.faq-[^{]*\{[^}]+\})', css):
    print(r)

print("\n=== KOTAVILA GALLERY RULES ===")
for r in re.findall(r'(\.kotavila-gallery[^{]*\{[^}]+\})', css):
    print(r)

with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

print("\n=== FAQ ACCORDION JS ===")
for line in js.splitlines():
    if 'faq' in line.lower() or 'accordion' in line.lower():
        print(line)
