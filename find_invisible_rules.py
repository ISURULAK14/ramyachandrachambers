with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'([^{}]*\{[^}]*(?:opacity\s*:\s*0|display\s*:\s*none|visibility\s*:\s*hidden)[^}]*\})', css)
print(f"Found {len(matches)} rules with opacity:0 / display:none / visibility:hidden:")
for m in matches:
    print("--------------------------------------------------")
    print(m)
