import glob

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('href="style.css"', 'href="style.css?v=6"')
    content = content.replace('href="style.css?v=5"', 'href="style.css?v=6"')
    content = content.replace('app.js?v=5', 'app.js?v=6')
    content = content.replace('app.js?v=4', 'app.js?v=6')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated style.css and app.js version to v=6")
