with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
m = re.findall(r'(\w*IntersectionObserver[^\n]+)', js)
print("IntersectionObserver lines:", m)

for idx, line in enumerate(js.split('\n')):
    if 'IntersectionObserver' in line or 'reveal' in line:
        print(f"{idx+1}: {line}")
