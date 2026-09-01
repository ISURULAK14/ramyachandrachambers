import shutil
import os
import glob

src_dir = os.path.abspath(".")
dest_dir = "C:\\Users\\isuru\\Desktop\\anti web"

# Sync all production files
prod_patterns = ['*.html', 'css/*.css', 'js/*.js', '*.svg']

for pat in prod_patterns:
    for src_file in glob.glob(os.path.join(src_dir, pat)):
        rel = os.path.relpath(src_file, src_dir)
        dest_file = os.path.join(dest_dir, rel)
        os.makedirs(os.path.dirname(dest_file), exist_ok=True)
        shutil.copy2(src_file, dest_file)
        print(f"Synced {rel} -> {dest_dir}")

print("Sync completed successfully.")
