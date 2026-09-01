with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
m = re.findall(r'(#(?:services|practice-areas|testimonials|contact)[^{]*\{[^}]+\})', css)
print("Section ID rules in CSS:")
for r in m:
    print(r)

m_class = re.findall(r'(\.(?:services|practice-areas|testimonials|contact)[a-z-]*[^{]*\{[^}]+\})', css)
print("\nSection Class rules in CSS:")
for r in m_class:
    print(r)
