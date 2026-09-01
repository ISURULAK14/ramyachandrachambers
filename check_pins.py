with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
pins = re.findall(r'(\.pin-[a-z0-9-]+[^{]*\{[^}]+\})', css)
print(f"Found {len(pins)} pin position rules in CSS:")
for p in pins[:10]:
    print(" ", p)
