import re
import glob

# 1. Update css/style.css: set inactive .map-pin opacity to 0
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .map-pin opacity:0.85 or opacity:.72 with opacity: 0
css = re.sub(r'(\.map-pin\s*\{[^}]*opacity\s*:\s*)[0-9.]+', r'\g<1>0', css)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("1. Updated css/style.css: Inactive .map-pin opacity set to 0.")

# 2. Update footers across all HTML pages
html_files = glob.glob('*.html')

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match the whole footer-nav and replace with just the privacy/terms row
    new_footer_nav = """            <!-- Middle: Legal Modals Navigation -->
            <nav class="footer-nav" aria-label="Footer Legal Navigation">
                <div class="footer-nav-row">
                    <a href="#" id="open-privacy-link" class="footer-link" role="button" aria-haspopup="dialog">Privacy Policy</a>
                    <a href="#" id="open-terms-link" class="footer-link" role="button" aria-haspopup="dialog">Terms of Engagement</a>
                </div>
            </nav>"""
    
    old_nav_pattern = r'<nav class="footer-nav"[^>]*>.*?</nav>'
    if re.search(old_nav_pattern, content, re.DOTALL):
        updated_content = re.sub(old_nav_pattern, new_footer_nav, content, flags=re.DOTALL)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"2. Updated footer in {fpath}")

print("All changes applied successfully.")
