import subprocess

res = subprocess.run(['git', 'show', '7f6755e:about.html'], capture_output=True)
html = res.stdout.decode('utf-8', errors='ignore')

start = html.find('<!-- World Map Sequence Animation')
end = html.find('</script>', start) + 9

print(html[start:end])
