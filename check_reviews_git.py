import subprocess

# Let's inspect testimonials/review boxes across git history
commits = ['0ed49c3', '3eaa051', '7f6755e', '0c9bd10', '2860110']

for c in commits:
    res = subprocess.run(['git', 'show', f'{c}:index.html'], capture_output=True)
    html = res.stdout.decode('utf-8', errors='ignore')
    t_start = html.find('id="testimonials"')
    if t_start != -1:
        t_end = html.find('</section>', t_start)
        print(f"=== TESTIMONIALS IN COMMIT {c} ===")
        print(html[t_start:t_start+800])
