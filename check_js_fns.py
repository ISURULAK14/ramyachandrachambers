with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
m = re.findall(r'(function\s+init[A-Za-z0-9_]+\s*\([^)]*\)\s*\{[^}]+\})', js)
for fn in m:
    print(fn[:100])
