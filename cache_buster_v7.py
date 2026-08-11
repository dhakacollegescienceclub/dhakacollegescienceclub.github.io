import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Safely replace v=6 with v=7
    content = content.replace('v=6', 'v=7')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated cache buster to v=7 in {len(html_files)} files.")
