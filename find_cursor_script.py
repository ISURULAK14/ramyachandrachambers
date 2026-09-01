import subprocess
import glob

# Search for cursor in all local files
for fpath in glob.glob('**/*', recursive=True):
    if fpath.endswith(('.html', '.js', '.css', '.py')):
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                c = f.read()
            if 'cursor' in c.lower() and ('pixel' in c.lower() or 'trail' in c.lower() or 'ambient' in c.lower() or 'mouse' in c.lower()):
                print(f"Match in {fpath}")
        except:
            pass

# Check commit 0ed49c3
res = subprocess.run(['git', 'show', '0ed49c3:js/main.js'], capture_output=True)
js_0ed = res.stdout.decode('utf-8', errors='ignore')
for line in js_0ed.splitlines():
    if any(k in line.lower() for k in ['cursor', 'ambient', 'canvas', 'particle', 'mouse']):
        print("0ed49c3 js/main.js:", line)

# Check orig_index.html
with open('orig_index.html', 'r', encoding='utf-8') as f:
    orig = f.read()
for line in orig.splitlines():
    if any(k in line.lower() for k in ['cursor', 'ambient', 'canvas', 'particle', 'mouse']):
        print("orig_index.html:", line)
