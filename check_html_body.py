with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
m = re.findall(r'((?:html|body)[^{]*\{[^}]+\})', css)
print("html / body rules in CSS:")
for r in m:
    print(" ", r)
