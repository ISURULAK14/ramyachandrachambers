import subprocess

res1 = subprocess.run(['git', 'show', '7f6755e:js/main.js'], capture_output=True)
code1 = res1.stdout.decode('utf-8', errors='ignore')

res2 = subprocess.run(['git', 'show', 'a2c7a22:js/main.js'], capture_output=True)
code2 = res2.stdout.decode('utf-8', errors='ignore')

print("--- Commit 7f6755e map code ---")
for line in code1.split('\n'):
    if 'cohort' in line or 'stepTimers' in line or '500' in line or 'pin-' in line:
        print(line)

print("\n--- Commit a2c7a22 map code ---")
for line in code2.split('\n'):
    if 'cohort' in line or 'stepTimers' in line or '500' in line or 'pin-' in line:
        print(line)
