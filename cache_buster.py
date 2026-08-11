import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('src="app.js"', 'src="app.js?v=4"')
    content = content.replace('src="app.js?v=2"', 'src="app.js?v=4"')
    content = content.replace('src="app.js?v=3"', 'src="app.js?v=4"')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated all HTML files successfully.")
