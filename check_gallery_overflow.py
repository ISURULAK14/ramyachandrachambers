with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
print("Office card overflow rules:")
for r in re.findall(r'(\.office-card[^{]*\{[^}]+\})', css):
    if 'overflow' in r:
        print(" ", r)

print("\nFort gallery rules:")
for r in re.findall(r'(\.fort-gallery[^{]*\{[^}]+\})', css):
    print(" ", r)

print("\nKotavila gallery rules:")
for r in re.findall(r'(\.kotavila-gallery[^{]*\{[^}]+\})', css):
    print(" ", r)
