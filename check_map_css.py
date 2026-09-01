with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
print("=== MAP WRAPPER RULES ===")
for r in re.findall(r'(\.map-[^{]*\{[^}]+\})', css):
    print(r)
