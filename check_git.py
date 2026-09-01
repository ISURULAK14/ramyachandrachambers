import subprocess

res = subprocess.run(['git', 'log', '-n', '25', '--oneline'], capture_output=True, text=True)
print("Git log:")
print(res.stdout)
