import subprocess
import re

res = subprocess.run(['git', 'show', '0ed49c3:css/style.css'], capture_output=True)
css_old = res.stdout.decode('utf-8', errors='ignore')

with open('css/style.css', 'r', encoding='utf-8') as f:
    css_curr = f.read()

m_old = re.findall(r'(\.review[^{]*\{[^}]+\})', css_old)
m_curr = re.findall(r'(\.review[^{]*\{[^}]+\})', css_curr)

print("Old review rules:")
for r in m_old:
    print(" ", r)

print("\nCurrent review rules:")
for r in m_curr:
    print(" ", r)
