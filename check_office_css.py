with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
rules = [
    r'(--location-card-padding[^{]*\{[^}]+\})',
    r'(\.fort-gallery[^{]*\{[^}]+\})',
    r'(\.kotavila-gallery[^{]*\{[^}]+\})',
    r'(\.map-container[^{]*\{[^}]+\})',
    r'(\.office-card-1[^{]*\{[^}]+\})',
    r'(\.office-detail[^{]*\{[^}]+\})',
    r'(:root[^{]*\{[^}]+\})'
]

for pat in rules:
    m = re.findall(pat, css)
    print(f"Match for {pat}:")
    for r in m:
        print(" ", r[:200])
