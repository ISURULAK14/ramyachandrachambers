with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
pins = re.findall(r'([^{}]*\.map-pin[^{]*\{[^}]+\})', css)
print(f"Found {len(pins)} .map-pin rules in CSS:")
for p in pins:
    print("--------------------------------------------------")
    print(p)
