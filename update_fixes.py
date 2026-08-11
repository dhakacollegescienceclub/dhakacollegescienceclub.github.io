import re

# 1. Update achievements.html
with open('achievements.html', 'r', encoding='utf-8') as f:
    ach_content = f.read()

# I will inject image/a1.jpg to a5.jpg inside the timeline-content div.
# We have 5 timeline items for now, so I'll find all <div class="timeline-content">...</div> and inject img at the end.
def inject_img(match):
    global idx
    if idx <= 5:
        img_tag = f'\n                            <img src="image/a{idx}.jpg" alt="Achievement {idx}" style="width: 100%; max-width: 500px; display: block; border-radius: 12px; margin-top: 20px; border: 1px solid rgba(0, 240, 255, 0.2); box-shadow: 0 5px 15px rgba(0,0,0,0.3);">'
        idx += 1
        return match.group(1) + img_tag + '\n                        </div>'
    return match.group(0)

idx = 1
# match everything up to the closing </div> of timeline-content
ach_content = re.sub(r'(<div class="timeline-content">[\s\S]*?)(?=\n\s*</div>\n\s*</div>\s*<!-- A[2-6]?)', inject_img, ach_content)

# To be safe and simpler, let's just do an explicit replace for each date/title since they are unique.
ach_replacements = [
    ("Afnan Bhuiya Nabil!</p>", f"Afnan Bhuiya Nabil!</p>\n                            <img src=\"image/a1.jpg\" style=\"width: 100%; border-radius: 12px; margin-top: 15px; border: 1px solid rgba(0,242,254,0.3);\">"),
    ("( Ideal School and College).</p>", f"( Ideal School and College).</p>\n                            <img src=\"image/a2.jpg\" style=\"width: 100%; border-radius: 12px; margin-top: 15px; border: 1px solid rgba(0,242,254,0.3);\">"),
    ("Dhaka College Science Club (DCSC)!</p>", f"Dhaka College Science Club (DCSC)!</p>\n                            <img src=\"image/a3.jpg\" style=\"width: 100%; border-radius: 12px; margin-top: 15px; border: 1px solid rgba(0,242,254,0.3);\">"),
    ("Champion of the Quiz Competition.</p>", f"Champion of the Quiz Competition.</p>\n                            <img src=\"image/a4.jpg\" style=\"width: 100%; border-radius: 12px; margin-top: 15px; border: 1px solid rgba(0,242,254,0.3);\">"),
    ("Afnan Bhuiya Nabil for being the Champions!</p>", f"Afnan Bhuiya Nabil for being the Champions!</p>\n                            <img src=\"image/a5.jpg\" style=\"width: 100%; border-radius: 12px; margin-top: 15px; border: 1px solid rgba(0,242,254,0.3);\">")
]

# Reload and apply explicit replacements for accuracy
with open('achievements.html', 'r', encoding='utf-8') as f:
    ach_content = f.read()
    
for target, replacement in ach_replacements:
    ach_content = ach_content.replace(target, replacement)
    
with open('achievements.html', 'w', encoding='utf-8') as f:
    f.write(ach_content)
print("Achievements updated")


# 2. Update index.html (Recap heading left-align and size up)
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Left align heading
header_target = """<div class="section-header">
                    <span class="section-subtitle">A YEAR TO REMEMBER</span>
                    <h2 class="section-title">2025 Recap</h2>
                    <div class="title-bar"></div>"""
header_repl = """<div class="section-header" style="text-align: left; align-items: flex-start;">
                    <span class="section-subtitle">A YEAR TO REMEMBER</span>
                    <h2 class="section-title">2025 Recap</h2>
                    <div class="title-bar" style="margin: 20px 0;"></div>"""
idx_content = idx_content.replace(header_target, header_repl)

# Increase size
# We'll replace the inline style for recap items
idx_content = re.sub(r'flex: 0 0 300px; height: 300px;', r'flex: 0 0 450px; height: 450px;', idx_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)
print("Index updated")


# 3. Update wall-magazine.html
with open('wall-magazine.html', 'r', encoding='utf-8') as f:
    wall_content = f.read()

# Generate exactly 27 images, 1:1, gapless grid
images_html = ""
for i in range(1, 28):
    images_html += f"""
                    <div style="aspect-ratio: 1/1; overflow: hidden;">
                        <img src="image/W{i}.jpg" alt="Wall Magazine {i}" style="width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    </div>"""

# Find the section and replace its content
new_grid = f"""<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 0; width: 100%; border: 1px solid var(--border-color); box-shadow: 0 10px 40px rgba(0,0,0,0.5);">{images_html}
                </div>"""

# Replace anything inside the main section for wall magazine
wall_content = re.sub(r'<div class="wonder-grid">.*?</div>\s*</div>\s*</section>', f'{new_grid}\n            </div>\n        </section>', wall_content, flags=re.DOTALL)

with open('wall-magazine.html', 'w', encoding='utf-8') as f:
    f.write(wall_content)
print("Wall magazine updated")

