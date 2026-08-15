import os, re

base_dir = r"c:\Users\USER\Downloads\DCSC"
domain = "https://dhakacollegescienceclub.github.io"
google_verification_code = "google12af7f296e1578d5"

# 1. Create robots.txt
robots_content = f"""User-agent: *
Allow: /

Sitemap: {domain}/sitemap.xml
"""

with open(os.path.join(base_dir, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_content)

# 2. Create sitemap.xml
pages = [
    ("index.html", "1.0", "daily"),
    ("about.html", "0.8", "weekly"),
    ("events.html", "0.8", "weekly"),
    ("achievements.html", "0.8", "monthly"),
    ("committee.html", "0.8", "monthly"),
    ("gallery.html", "0.8", "weekly"),
    ("posts.html", "0.8", "daily"),
    ("join.html", "0.9", "monthly"),
    ("scilab.html", "0.8", "monthly"),
    ("wall-magazine.html", "0.7", "monthly"),
    ("event-freshers.html", "0.6", "monthly"),
    ("event-neuroverse.html", "0.6", "monthly"),
    ("event-quizzing.html", "0.6", "monthly"),
    ("event-us.html", "0.6", "monthly"),
    ("scilab-chem.html", "0.6", "monthly"),
    ("scilab-atom.html", "0.6", "monthly"),
    ("scilab-gravity.html", "0.6", "monthly"),
    ("scilab-quiz.html", "0.6", "monthly"),
    ("cert-verify.html", "0.5", "monthly")
]

sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>',
'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

for p, priority, freq in pages:
    url_path = "" if p == "index.html" else p
    sitemap_xml.append("  <url>")
    sitemap_xml.append(f"    <loc>{domain}/{url_path}</loc>")
    sitemap_xml.append("    <lastmod>2026-08-15</lastmod>")
    sitemap_xml.append(f"    <changefreq>{freq}</changefreq>")
    sitemap_xml.append(f"    <priority>{priority}</priority>")
    sitemap_xml.append("  </url>")

sitemap_xml.append("</urlset>")

with open(os.path.join(base_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_xml))

# 3. WebSite Schema & EducationalOrganization Schema for Google Site Name
json_ld_website = f"""
    <!-- Google WebSite Schema for Site Name -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "Dhaka College Science Club",
      "alternateName": ["DCSC", "Dhaka College Science Club (DCSC)"],
      "url": "{domain}/"
    }}
    </script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "EducationalOrganization",
      "name": "Dhaka College Science Club",
      "alternateName": "DCSC",
      "url": "{domain}/",
      "logo": "{domain}/image/logo.png",
      "foundingDate": "1996",
      "description": "Spreading the knowledge of science to the utmost since 1996.",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "Dhaka",
        "addressCountry": "BD"
      }},
      "sameAs": [
        "https://www.facebook.com/DhakaCollegeScienceClub",
        "https://www.instagram.com/dcsc_official"
      ]
    }}
    </script>"""

html_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

for filename in html_files:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Determine canonical URL
    page_url = f"{domain}/" if filename == "index.html" else f"{domain}/{filename}"

    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    page_title = title_match.group(1) if title_match else "Dhaka College Science Club (DCSC)"

    # Clean existing SEO meta tags
    content = re.sub(r'<meta\s+name=["\']google-site-verification["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+name=["\']description["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+name=["\']keywords["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+name=["\']robots["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+name=["\']author["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+name=["\']theme-color["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+property=["\']og:[^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+property=["\']twitter:[^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<link\s+rel=["\'](icon|shortcut icon|apple-touch-icon|canonical)["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<script\s+type=["\']application/ld\+json["\'][^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)

    seo_block = f"""
    <!-- Google Search Console Verification -->
    <meta name="google-site-verification" content="{google_verification_code}">

    <!-- SEO Meta Tags -->
    <meta name="description" content="Dhaka College Science Club (DCSC) — Spreading the knowledge of science to the utmost since 1996. Official website of DCSC.">
    <meta name="keywords" content="Dhaka College Science Club, DCSC, Dhaka College, Science Club Bangladesh, DCSC Official, Science Club">
    <meta name="robots" content="index, follow">
    <meta name="author" content="Dhaka College Science Club">
    <meta name="theme-color" content="#080C14">
    <link rel="canonical" href="{page_url}">

    <!-- Google & Bing Favicons -->
    <link rel="icon" type="image/x-icon" href="{domain}/favicon.ico">
    <link rel="shortcut icon" type="image/x-icon" href="{domain}/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="{domain}/image/favicon.png">
    <link rel="icon" type="image/png" sizes="192x192" href="{domain}/image/favicon.png">
    <link rel="apple-touch-icon" sizes="180x180" href="{domain}/image/logo.png">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{page_url}">
    <meta property="og:title" content="{page_title}">
    <meta property="og:description" content="Dhaka College Science Club (DCSC) — Spreading the knowledge of science to the utmost since 1996. Discover events, science lab, achievements, and join DCSC.">
    <meta property="og:image" content="{domain}/image/logo.png">
    <meta property="og:site_name" content="Dhaka College Science Club">

    <!-- Twitter Cards -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="{page_url}">
    <meta property="twitter:title" content="{page_title}">
    <meta property="twitter:description" content="Dhaka College Science Club (DCSC) — Spreading the knowledge of science to the utmost since 1996.">
    <meta property="twitter:image" content="{domain}/image/logo.png">
{json_ld_website if filename == "index.html" else ""}"""

    # Insert seo_block right after <meta name="viewport" ...>
    if '<meta name="viewport"' in content:
        content = re.sub(r'(<meta\s+name=["\']viewport["\'][^>]*>)', r'\1\n' + seo_block, content, count=1, flags=re.IGNORECASE)
    elif '<head>' in content:
        content = re.sub(r'(<head[^>]*>)', r'\1\n' + seo_block, content, count=1, flags=re.IGNORECASE)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Updated HTML files with WebSite schema and root favicon icons.")
