with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
print("Site Nav rules:")
for r in re.findall(r'(\.site-nav[^{]*\{[^}]+\})', css):
    print(" ", r)

print("\nFooter rules:")
for r in re.findall(r'(\.site-footer[^{]*\{[^}]+\})', css):
    print(" ", r)

print("\nMedia queries:")
for m in re.findall(r'(@media[^{]+\{)', css):
    print(" ", m)
