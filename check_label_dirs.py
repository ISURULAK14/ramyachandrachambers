with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
m = re.findall(r'(\.pin-[a-z0-9-,\s]+\.pin-label\s*\{[^}]+\})', css)
for r in m:
    print(r)
