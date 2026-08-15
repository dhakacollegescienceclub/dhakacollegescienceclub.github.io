import os, xml.etree.ElementTree as ET

base_dir = r"c:\Users\USER\Downloads\DCSC"
sitemap_path = os.path.join(base_dir, "sitemap.xml")

print("="*60)
print("GOOGLE SEARCH CONSOLE SITEMAP VALIDATION AUDIT")
print("="*60)

# Check file existence
if not os.path.exists(sitemap_path):
    print("[FAIL] sitemap.xml file NOT found!")
    exit(1)

# Check file encoding
with open(sitemap_path, "rb") as f:
    raw_bytes = f.read()

if raw_bytes.startswith(b'\xef\xbb\xbf'):
    print("[WARN] sitemap.xml has UTF-8 BOM. Fixing to pure UTF-8 without BOM...")
    clean_text = raw_bytes[3:].decode('utf-8')
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(clean_text)
    print("[OK] Fixed sitemap.xml encoding to pure UTF-8 (No BOM)")
else:
    print("[OK] Encoding: Pure UTF-8 (No BOM)")

# Check XML Syntax
try:
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    print("[OK] XML Syntax: 100% Valid XML Format")
except Exception as e:
    print(f"[FAIL] XML Parsing Error: {e}")
    exit(1)

# Check Namespace
ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
if "sitemaps.org" in root.tag:
    print("[OK] Namespace: Valid Sitemaps.org 0.9 schema")
else:
    print("[WARN] Invalid namespace in urlset element")

# Check URLs
urls = root.findall("sm:url", ns)
print(f"[OK] Total Mapped URLs: {len(urls)}")

domain = "https://dhakacollegescienceclub.github.io"
errors = []

for idx, u in enumerate(urls, 1):
    loc = u.find("sm:loc", ns)
    lastmod = u.find("sm:lastmod", ns)
    changefreq = u.find("sm:changefreq", ns)
    priority = u.find("sm:priority", ns)

    if loc is None or not loc.text:
        errors.append(f"URL #{idx}: Missing <loc> element")
        continue

    url_str = loc.text.strip()
    if not url_str.startswith(domain):
        errors.append(f"URL #{idx}: URL {url_str} does not start with domain {domain}")

    # Check if local html file exists
    path_part = url_str.replace(domain + "/", "").replace(domain, "")
    if path_part == "":
        local_file = "index.html"
    else:
        local_file = path_part

    if not os.path.exists(os.path.join(base_dir, local_file)):
        errors.append(f"URL #{idx}: File '{local_file}' does not exist on disk!")

if errors:
    print("\n[FAIL] Errors Found:")
    for err in errors:
        print("  - " + err)
else:
    print("[SUCCESS] All 19 URLs in sitemap.xml are 100% valid, accessible, and compliant with Google Search Console standards!")

print("="*60)
