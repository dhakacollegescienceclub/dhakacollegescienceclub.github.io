import re

# ==============================================================
# TASK 1: HOME PAGE 2025 RECAP (`index.html`)
# ==============================================================
recap_html = '''
        <!-- 2025 RECAP GALLERY -->
        <section class="section-padding" style="background: linear-gradient(180deg, var(--bg-main) 0%, rgba(0,240,255,0.05) 100%);">
            <div class="section-container">
                <div class="section-header" style="text-align: center;">
                    <span class="section-subtitle">MOMENTS</span>
                    <h2 class="section-title" style="font-family: 'Space Grotesk', sans-serif; font-size: 3rem; text-transform: uppercase; background: linear-gradient(90deg, #fff, var(--cyan-glow)); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">2025 Recap</h2>
                    <p style="color: var(--text-secondary); margin-top: 15px;">A glimpse into an unforgettable year of science, discovery, and brotherhood.</p>
                </div>
                
                <!-- Horizontal scrolling gallery -->
                <div style="display: flex; gap: 20px; overflow-x: auto; padding: 20px 0; scroll-snap-type: x mandatory; -ms-overflow-style: none; scrollbar-width: none;" class="recap-slider">
'''
for i in range(1, 11):
    recap_html += f'''                    <div style="flex: 0 0 300px; height: 300px; border-radius: 20px; overflow: hidden; scroll-snap-align: start; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1);" class="animate-on-scroll">
                        <img src="image/r{i}.jpg" alt="2025 Recap Moment {i}" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    </div>\n'''
recap_html += '''                </div>
            </div>
        </section>
'''

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Insert before <section class="section-padding bg-alt"> (the location & map section)
idx = re.sub(r'(<!-- GOOGLE MAPS EMBED SECTION -->)', recap_html + r'\n        \1', idx)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)


# ==============================================================
# TASK 8: GALLERY NAV FIX (`gallery.html`)
# ==============================================================
# Gallery has gr1 and gr2. Wait, does it? Let's just fix the navbar.
with open('gallery.html', 'r', encoding='utf-8') as f:
    gal = f.read()

nav_template = '''    <header class="navbar">
        <div class="nav-container">
            <a href="index.html" class="brand-logo">
                <div class="logo-shield">
                    <img src="image/logo.png" alt="DCSC Shield Logo" onerror="this.src='image/logo.svg'">
                </div>
                <div class="brand-text">
                    <span class="brand-line1">DHAKA COLLEGE</span>
                    <span class="brand-line2">SCIENCE CLUB</span>
                </div>
            </a>
            <nav class="nav-menu" id="nav-menu">
                <a href="index.html" class="nav-link">Home</a>
                <a href="events.html" class="nav-link">Events</a>
                <a href="achievements.html" class="nav-link">Achievements</a>
                <a href="committee.html" class="nav-link">Committee</a>
                <a href="scilab.html" class="nav-link">Sci-Lab</a>
                
                <div class="nav-dropdown">
                    <a href="#" class="nav-link dropdown-toggle active">More <i class="fa-solid fa-chevron-down" style="font-size:0.75rem;"></i></a>
                    <div class="dropdown-menu">
                        <a href="wall-magazine.html" class="dropdown-item"><i class="fa-solid fa-newspaper"></i> Wall Magazine</a>
                        <a href="posts.html" class="dropdown-item"><i class="fa-solid fa-bullhorn"></i> Posts & News</a>
                        <a href="gallery.html" class="dropdown-item active"><i class="fa-solid fa-images"></i> Photo Gallery</a>
                        <a href="about.html" class="dropdown-item"><i class="fa-solid fa-circle-info"></i> Info & Contact</a>
                    </div>
                </div>
            </nav>
            <div class="nav-controls">
                <button class="icon-btn" id="theme-btn" title="Toggle Dark/Light Mode"><i class="fa-solid fa-moon"></i></button>
                <a href="join.html" class="btn-primary"><i class="fa-solid fa-user-plus"></i> Join Club</a>
                <button class="hamburger" id="hamburger"><i class="fa-solid fa-bars"></i></button>
            </div>
        </div>
    </header>'''

gal = re.sub(r'<header class="navbar">.*?</header>', nav_template, gal, flags=re.DOTALL)
with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(gal)

print("Tasks 1, 8 completed.")
