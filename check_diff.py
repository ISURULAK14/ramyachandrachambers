import subprocess

res = subprocess.run(['git', 'show', '7f6755e'], capture_output=True)
print(res.stdout.decode('utf-8', errors='ignore')[:3000])
