import os, re, json

base_dir = r"c:\Users\USER\Downloads\DCSC"
domain = "https://dhakacollegescienceclub.github.io"
google_verification_code = "google12af7f296e1578d5"

# Page configurations for titles, descriptions, breadcrumbs
page_configs = {
    "index.html": {
        "title": "Dhaka College Science Club (DCSC) | Official Website",
        "desc": "Dhaka College Science Club (DCSC) — Spreading the knowledge of science to the utmost since 1996. Official website of DCSC.",
        "breadcrumb_name": "Home",
        "priority": "1.0",
        "freq": "daily"
    },
    "about.html": {
        "title": "About Us | Dhaka College Science Club (DCSC)",
        "desc": "Learn about the history, mission, vision, and advisory body of Dhaka College Science Club (DCSC), established in 1996.",
        "breadcrumb_name": "About Us",
        "priority": "0.8",
        "freq": "weekly"
    },
    "events.html": {
        "title": "Events & Science Festivals | Dhaka College Science Club (DCSC)",
        "desc": "Discover upcoming and past science festivals, olympiads, workshops, and competitions organized by DCSC.",
        "breadcrumb_name": "Events",
        "priority": "0.8",
        "freq": "weekly"
    },
    "achievements.html": {
        "title": "Achievements & Awards | Dhaka College Science Club (DCSC)",
        "desc": "Explore national and international achievements, awards, and accolades won by DCSC members.",
        "breadcrumb_name": "Achievements",
        "priority": "0.8",
        "freq": "monthly"
    },
    "committee.html": {
        "title": "Executive Committee & Leaders | Dhaka College Science Club (DCSC)",
        "desc": "Meet the Executive Committee members, Moderators, Advisors, and leadership team of DCSC.",
        "breadcrumb_name": "Committee",
        "priority": "0.8",
        "freq": "monthly"
    },
    "gallery.html": {
        "title": "Photo Gallery | Dhaka College Science Club (DCSC)",
        "desc": "Browse photos and memories from DCSC science festivals, workshops, orientation programs, and events.",
        "breadcrumb_name": "Gallery",
        "priority": "0.8",
        "freq": "weekly"
    },
    "posts.html": {
        "title": "News, Updates & Posts | Dhaka College Science Club (DCSC)",
        "desc": "Stay updated with recent notices, science articles, event updates, and news from Dhaka College Science Club.",
        "breadcrumb_name": "Posts",
        "priority": "0.8",
        "freq": "daily"
    },
    "join.html": {
        "title": "Join DCSC & ID Card | Dhaka College Science Club (DCSC)",
        "desc": "Apply for membership in Dhaka College Science Club, generate your provisional digital Member ID card and certificates.",
        "breadcrumb_name": "Join Club",
        "priority": "0.9",
        "freq": "monthly"
    },
    "scilab.html": {
        "title": "Sci-Lab Interactive Games | Dhaka College Science Club (DCSC)",
        "desc": "Play interactive science games: Chemistry Reactions, Atom Builder, Gravity Simulator, and Science Quizzes.",
        "breadcrumb_name": "Sci-Lab",
        "priority": "0.8",
        "freq": "monthly"
    },
    "wall-magazine.html": {
        "title": "Wall Magazine | Dhaka College Science Club (DCSC)",
        "desc": "Explore creative wall magazine publications, science write-ups, and student research articles by DCSC.",
        "breadcrumb_name": "Wall Magazine",
        "priority": "0.7",
        "freq": "monthly"
    },
    "event-freshers.html": {
        "title": "Freshers' Orientation 2025 | Dhaka College Science Club (DCSC)",
        "desc": "Details and highlights of the DCSC Freshers' Orientation & Science Fest 2025.",
        "breadcrumb_name": "Freshers Orientation",
        "priority": "0.6",
        "freq": "monthly"
    },
    "event-neuroverse.html": {
        "title": "Neuroverse 2025 | Dhaka College Science Club (DCSC)",
        "desc": "Explore Neuroverse 2025 — National Neuroscience Olympiad & Competition organized by DCSC.",
        "breadcrumb_name": "Neuroverse 2025",
        "priority": "0.6",
        "freq": "monthly"
    },
    "event-quizzing.html": {
        "title": "Intra Quizzing Festival | Dhaka College Science Club (DCSC)",
        "desc": "Intra Dhaka College Science Quizzing Festival — Test your knowledge in Physics, Chemistry, Biology, and ICT.",
        "breadcrumb_name": "Quizzing Festival",
        "priority": "0.6",
        "freq": "monthly"
    },
    "event-us.html": {
        "title": "Upcoming Science Festival | Dhaka College Science Club (DCSC)",
        "desc": "Information regarding upcoming national science carnivals and club events.",
        "breadcrumb_name": "Science Festival",
        "priority": "0.6",
        "freq": "monthly"
    },
    "scilab-chem.html": {
        "title": "Chemistry Reaction Lab | Sci-Lab DCSC",
        "desc": "Mix chemicals virtually and discover fascinating chemical reactions in DCSC Sci-Lab.",
        "breadcrumb_name": "Chemistry Lab",
        "priority": "0.6",
        "freq": "monthly"
    },
    "scilab-atom.html": {
        "title": "Atom Builder | Sci-Lab DCSC",
        "desc": "Build atomic models by adding protons, neutrons, and electrons in DCSC Sci-Lab.",
        "breadcrumb_name": "Atom Builder",
        "priority": "0.6",
        "freq": "monthly"
    },
    "scilab-gravity.html": {
        "title": "Gravity Simulator | Sci-Lab DCSC",
        "desc": "Simulate gravitational forces between celestial bodies in space with DCSC Sci-Lab.",
        "breadcrumb_name": "Gravity Simulator",
        "priority": "0.6",
        "freq": "monthly"
    },
    "scilab-quiz.html": {
        "title": "Science Quiz Challenge | Sci-Lab DCSC",
        "desc": "Test your science knowledge with interactive quizzes across multiple scientific domains.",
        "breadcrumb_name": "Science Quiz",
        "priority": "0.6",
        "freq": "monthly"
    },
    "scilab-reaction.html": {
        "title": "Chemical Reaction Simulator | Sci-Lab DCSC",
        "desc": "Simulate complex chemical equations and lab experiments virtually.",
        "breadcrumb_name": "Reaction Lab",
        "priority": "0.6",
        "freq": "monthly"
    },
    "scilab-sandbox.html": {
        "title": "Physics Sandbox | Sci-Lab DCSC",
        "desc": "Experiment with physics particles and gravity forces in real-time.",
        "breadcrumb_name": "Physics Sandbox",
        "priority": "0.6",
        "freq": "monthly"
    },
    "cert-verify.html": {
        "title": "Verify Certificate | Dhaka College Science Club (DCSC)",
        "desc": "Verify authentic DCSC participation and achievement certificates instantly.",
        "breadcrumb_name": "Verify Certificate",
        "priority": "0.5",
        "freq": "monthly"
    },
    "certificates.html": {
        "title": "Certificate Portal | Dhaka College Science Club (DCSC)",
        "desc": "Access and verify member certificates for DCSC events.",
        "breadcrumb_name": "Certificates",
        "priority": "0.5",
        "freq": "monthly"
    }
}

# 1. Generate robots.txt
robots_content = f"""User-agent: *
Allow: /

Sitemap: {domain}/sitemap.xml
"""

with open(os.path.join(base_dir, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_content)
print("robots.txt updated.")

# 2. Generate sitemap.xml
sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>',
'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

for p, cfg in page_configs.items():
    url_path = "" if p == "index.html" else p
    sitemap_xml.append("  <url>")
    sitemap_xml.append(f"    <loc>{domain}/{url_path}</loc>")
    sitemap_xml.append("    <lastmod>2026-08-17</lastmod>")
    sitemap_xml.append(f"    <changefreq>{cfg['freq']}</changefreq>")
    sitemap_xml.append(f"    <priority>{cfg['priority']}</priority>")
    sitemap_xml.append("  </url>")

sitemap_xml.append("</urlset>")

with open(os.path.join(base_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_xml))
print("sitemap.xml updated.")

# 3. Process all HTML files
html_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

for filename in html_files:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    cfg = page_configs.get(filename, {
        "title": "Dhaka College Science Club (DCSC)",
        "desc": "Spreading the knowledge of science to the utmost since 1996.",
        "breadcrumb_name": filename.replace(".html", "").replace("-", " ").title()
    })

    page_url = f"{domain}/" if filename == "index.html" else f"{domain}/{filename}"

    # Replace title
    content = re.sub(r'<title>(.*?)</title>', f'<title>{cfg["title"]}</title>', content, flags=re.IGNORECASE)

    # Clean existing SEO meta tags
    content = re.sub(r'<meta\s+name=["\']google-site-verification["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+name=["\']description["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+name=["\']keywords["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+name=["\']robots["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+name=["\']author["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+name=["\']publisher["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+name=["\']application-name["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+name=["\']apple-mobile-web-app-title["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+name=["\']theme-color["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+property=["\']og:[^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta\s+property=["\']twitter:[^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<link\s+rel=["\'](icon|shortcut icon|apple-touch-icon|canonical|manifest)["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<script\s+type=["\']application/ld\+json["\'][^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)

    # Build Breadcrumb JSON-LD
    breadcrumb_items = [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": f"{domain}/"
        }
    ]
    if filename != "index.html":
        breadcrumb_items.append({
            "@type": "ListItem",
            "position": 2,
            "name": cfg["breadcrumb_name"],
            "item": page_url
        })

    breadcrumb_json = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": breadcrumb_items
    }

    # WebSite & Organization JSON-LD
    website_json = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Dhaka College Science Club (DCSC)",
        "alternateName": ["DCSC", "Dhaka College Science Club"],
        "url": f"{domain}/",
        "publisher": {
            "@type": "Organization",
            "name": "Dhaka College Science Club (DCSC)",
            "logo": f"{domain}/image/logo.png"
        }
    }

    org_json = {
        "@context": "https://schema.org",
        "@type": "EducationalOrganization",
        "name": "Dhaka College Science Club (DCSC)",
        "alternateName": "DCSC",
        "url": f"{domain}/",
        "logo": f"{domain}/image/logo.png",
        "foundingDate": "1996",
        "description": "Spreading the knowledge of science to the utmost since 1996.",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Dhaka",
            "addressCountry": "BD"
        },
        "sameAs": [
            "https://www.facebook.com/DhakaCollegeScienceClub",
            "https://www.instagram.com/dcsc_official"
        ]
    }

    seo_block = f"""
    <!-- Google Search Console Verification -->
    <meta name="google-site-verification" content="{google_verification_code}">

    <!-- Application & Site Name Meta Tags for Google & Bing -->
    <meta name="application-name" content="Dhaka College Science Club (DCSC)">
    <meta name="apple-mobile-web-app-title" content="DCSC">
    <meta name="publisher" content="Dhaka College Science Club (DCSC)">

    <!-- SEO Meta Tags -->
    <meta name="description" content="{cfg['desc']}">
    <meta name="keywords" content="Dhaka College Science Club, DCSC, Dhaka College, Science Club Bangladesh, DCSC Official, Science Club">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="author" content="Dhaka College Science Club (DCSC)">
    <meta name="theme-color" content="#080C14">
    <link rel="canonical" href="{page_url}">

    <!-- Complete Favicon Suite (SVG, ICO, Multi-size PNG & WebManifest) -->
    <link rel="icon" type="image/svg+xml" href="{domain}/favicon.svg">
    <link rel="icon" type="image/x-icon" href="{domain}/favicon.ico">
    <link rel="shortcut icon" type="image/x-icon" href="{domain}/favicon.ico">
    <link rel="icon" type="image/png" sizes="16x16" href="{domain}/favicon-16x16.png">
    <link rel="icon" type="image/png" sizes="32x32" href="{domain}/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="192x192" href="{domain}/android-chrome-192x192.png">
    <link rel="icon" type="image/png" sizes="512x512" href="{domain}/android-chrome-512x512.png">
    <link rel="apple-touch-icon" sizes="180x180" href="{domain}/apple-touch-icon.png">
    <link rel="manifest" href="{domain}/site.webmanifest">

    <!-- Open Graph / Facebook / WhatsApp / LinkedIn / Instagram -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{page_url}">
    <meta property="og:title" content="{cfg['title']}">
    <meta property="og:description" content="{cfg['desc']}">
    <meta property="og:image" content="{domain}/image/logo.png">
    <meta property="og:image:secure_url" content="{domain}/image/logo.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:type" content="image/png">
    <meta property="og:image:alt" content="Dhaka College Science Club (DCSC) Logo">
    <meta property="og:site_name" content="Dhaka College Science Club (DCSC)">
    <meta property="og:locale" content="en_US">

    <!-- Twitter Cards -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="{page_url}">
    <meta property="twitter:title" content="{cfg['title']}">
    <meta property="twitter:description" content="{cfg['desc']}">
    <meta property="twitter:image" content="{domain}/image/logo.png">

    <!-- Schema.org JSON-LD (Site Name, Organization & Breadcrumb Navigation) -->
    <script type="application/ld+json">
    {json.dumps(website_json, indent=2)}
    </script>
    <script type="application/ld+json">
    {json.dumps(org_json, indent=2)}
    </script>
    <script type="application/ld+json">
    {json.dumps(breadcrumb_json, indent=2)}
    </script>"""

    # Insert seo_block right after <meta name="viewport" ...>
    if '<meta name="viewport"' in content:
        content = re.sub(r'(<meta\s+name=["\']viewport["\'][^>]*>)', r'\1\n' + seo_block, content, count=1, flags=re.IGNORECASE)
    elif '<head>' in content:
        content = re.sub(r'(<head[^>]*>)', r'\1\n' + seo_block, content, count=1, flags=re.IGNORECASE)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Master SEO & Site Name Optimization completed for {len(html_files)} HTML files!")
