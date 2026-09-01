import subprocess

res = subprocess.run(['git', 'show', '0ed49c3:index.html'], capture_output=True)
html = res.stdout.decode('utf-8', errors='ignore')

t_start = html.find('class="reviews-container"')
if t_start == -1:
    t_start = html.find('class="review')
if t_start == -1:
    t_start = html.find('id="testimonials"')

t_end = html.find('</section>', t_start)
print(html[t_start:t_end])
