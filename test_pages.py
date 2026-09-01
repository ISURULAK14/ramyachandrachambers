import urllib.request, os, sys
base = 'http://localhost:8000/'
failed = False
for f in os.listdir('.'): 
    if f.endswith('.html'):
        try:
            with urllib.request.urlopen(base + f, timeout=10) as resp:
                print(f"{f}: {resp.getcode()}")
        except Exception as e:
            print(f"{f}: Failed ({e})")
            failed = True
if failed:
    sys.exit(1)
else:
    sys.exit(0)
