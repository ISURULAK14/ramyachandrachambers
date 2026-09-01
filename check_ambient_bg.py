with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
print("=== AMBIENT / CANVAS CSS RULES ===")
for r in re.findall(r'(\.[a-z0-9-_]*ambient[^{]*\{[^}]+\})', css, re.IGNORECASE):
    print(r)
for r in re.findall(r'(\.ambient-cosmos-canvas[^{]*\{[^}]+\})', css, re.IGNORECASE):
    print(r)
for r in re.findall(r'(\.global-ambient-system[^{]*\{[^}]+\})', css, re.IGNORECASE):
    print(r)

print("\n=== JS CANVAS CODE ===")
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

for line in js.splitlines():
    if any(k in line.lower() for k in ['cosmos', 'ambient', 'particle', 'canvas']):
        print(line)
