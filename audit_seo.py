import os, json, re, xml.etree.ElementTree as ET

base_dir = r"c:\Users\USER\Downloads\DCSC"
domain = "https://dhakacollegescienceclub.github.io"

print("="*60)
print("STARTING FULL COMPREHENSIVE SEO & WEBSITE AUDIT")
print("="*60)

# 1. Check Root Favicon & Verification Files
required_files = [
    "favicon.ico",
    "favicon.png",
    "favicon.svg",
    "favicon-16x16.png",
    "favicon-32x32.png",
    "apple-touch-icon.png",
    "android-chrome-192x192.png",
    "android-chrome-512x512.png",
    "site.webmanifest",
    "robots.txt",
    "sitemap.xml",
    "google12af7f296e1578d5.html"
]

missing_files = []
for file in required_files:
    if os.path.exists(os.path.join(base_dir, file)):
        print(f"[OK] Root File Present: {file}")
    else:
        print(f"[FAIL] Missing File: {file}")
        missing_files.append(file)

print("-" * 60)

# 2. Check site.webmanifest JSON validity
manifest_path = os.path.join(base_dir, "site.webmanifest")
if os.path.exists(manifest_path):
    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        print("[OK] site.webmanifest: Valid JSON format")
    except Exception as e:
        print(f"[FAIL] site.webmanifest JSON error: {e}")

# 3. Check robots.txt content
robots_path = os.path.join(base_dir, "robots.txt")
if os.path.exists(robots_path):
    with open(robots_path, "r", encoding="utf-8") as f:
        robots = f.read()
    if "Sitemap:" in robots and "Allow: /" in robots:
        print("[OK] robots.txt: Correct User-agent and Sitemap directive")
    else:
        print("[WARN] robots.txt might be missing Sitemap directive")

# 4. Check sitemap.xml validity
sitemap_path = os.path.join(base_dir, "sitemap.xml")
if os.path.exists(sitemap_path):
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        urls = root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url")
        print(f"[OK] sitemap.xml: Valid XML with {len(urls)} URLs mapped")
    except Exception as e:
        print(f"[FAIL] sitemap.xml XML parsing error: {e}")

print("-" * 60)

# 5. Check all HTML files for SEO tags, favicons, Google Verification, Schema.org
html_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

checked_html = 0
passed_html = 0

for hfile in html_files:
    checked_html += 1
    hpath = os.path.join(base_dir, hfile)
    with open(hpath, "r", encoding="utf-8") as f:
        content = f.read()

    issues = []
    if "google12af7f296e1578d5" not in content:
        issues.append("Missing Google Verification tag")
    if "canonical" not in content:
        issues.append("Missing Canonical link")
    if "favicon.svg" not in content:
        issues.append("Missing SVG favicon link")
    if "favicon.ico" not in content:
        issues.append("Missing ICO favicon link")
    if "apple-touch-icon.png" not in content:
        issues.append("Missing Apple Touch Icon link")
    if "site.webmanifest" not in content:
        issues.append("Missing site.webmanifest link")
    if "og:title" not in content or "og:site_name" not in content:
        issues.append("Missing Open Graph tags")
    if "twitter:card" not in content:
        issues.append("Missing Twitter Card tags")

    if hfile == "index.html":
        if "schema.org" not in content or "WebSite" not in content:
            issues.append("Missing WebSite Schema JSON-LD")

    if issues:
        print(f"[WARN] {hfile}: Issues found -> {', '.join(issues)}")
    else:
        passed_html += 1

print(f"[SUCCESS] HTML Audit Passed: {passed_html} / {checked_html} HTML files fully compliant!")
print("="*60)
print("ALL COMPREHENSIVE CHECKS COMPLETED!")
print("="*60)
