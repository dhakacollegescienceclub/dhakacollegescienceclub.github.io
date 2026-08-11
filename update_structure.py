import os, glob

# 1. Rename/Copy achievements.html to posts.html
if os.path.exists('achievements.html'):
    with open('achievements.html', 'r', encoding='utf-8') as f:
        content = f.read()
    with open('posts.html', 'w', encoding='utf-8') as f:
        f.write(content.replace('<title>Achievements & Posts |', '<title>Posts & News |').replace('Achievements & News Feed', 'Posts & News Feed').replace('achievements.html" class="nav-link active"', 'achievements.html" class="nav-link"').replace('posts.html" class="dropdown-item"', 'posts.html" class="dropdown-item active"'))

# 2. Reset achievements.html to a clean state
empty_achievements = '''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Achievements | Dhaka College Science Club</title>
    <link rel="icon" type="image/png" href="image/favicon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&family=Orbitron:wght@700;800;900&family=Outfit:wght@500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <canvas id="bg-canvas"></canvas>
    <div class="cursor-glow" id="cursor-glow"></div>

    <header class="navbar">
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
                <a href="achievements.html" class="nav-link active">Achievements</a>
                <a href="committee.html" class="nav-link">Committee</a>
                <a href="scilab.html" class="nav-link">Sci-Lab</a>
                
                <div class="nav-dropdown">
                    <a href="#" class="nav-link dropdown-toggle">More <i class="fa-solid fa-chevron-down" style="font-size:0.75rem;"></i></a>
                    <div class="dropdown-menu">
                        <a href="wall-magazine.html" class="dropdown-item"><i class="fa-solid fa-newspaper"></i> Wall Magazine</a>
                        <a href="posts.html" class="dropdown-item"><i class="fa-solid fa-bullhorn"></i> Posts & News</a>
                        <a href="gallery.html" class="dropdown-item"><i class="fa-solid fa-images"></i> Photo Gallery</a>
                        <a href="about.html" class="dropdown-item"><i class="fa-solid fa-circle-info"></i> Info & Contact</a>
                    </div>
                </div>
            </nav>
            <div class="nav-controls">
                <button class="icon-btn" id="sound-btn" title="Toggle Theme Song"><i class="fa-solid fa-volume-xmark"></i></button>
                <button class="icon-btn" id="theme-btn" title="Toggle Dark/Light Mode"><i class="fa-solid fa-moon"></i></button>
                <a href="join.html" class="btn-primary"><i class="fa-solid fa-user-plus"></i> Join Club</a>
                <button class="hamburger" id="hamburger"><i class="fa-solid fa-bars"></i></button>
            </div>
        </div>
    </header>

    <main>
        <section class="page-banner">
            <h1 class="page-title">Achievements</h1>
            <p class="page-subtitle">Hall of Fame of Dhaka College Science Club</p>
        </section>

        <section class="section-padding">
            <div class="section-container" style="text-align: center; min-height: 40vh; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                <i class="fa-solid fa-trophy" style="font-size: 5rem; color: var(--gold-accent); margin-bottom: 20px;"></i>
                <h2 style="color: var(--text-primary); font-size: 2rem;">Achievements Gallery Coming Soon!</h2>
                <p style="color: var(--text-secondary); max-width: 600px; margin-top: 15px;">We are currently gathering all the glorious achievements of our club members. Stay tuned for updates!</p>
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="footer-container">
            <div class="footer-col">
                <div class="footer-logo">
                    <img src="image/logo.png" alt="DCSC Logo" onerror="this.src='image/logo.svg'">
                    <div class="brand-text">
                        <span class="brand-line1">DHAKA COLLEGE</span>
                        <span class="brand-line2">SCIENCE CLUB</span>
                    </div>
                </div>
                <p>Spreading the knowledge of science to the utmost since 1996. #ForClubAndCountry</p>
            </div>
            <div class="footer-col">
                <h4>Quick Navigation</h4>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="events.html">Events</a></li>
                    <li><a href="achievements.html">Achievements</a></li>
                    <li><a href="scilab.html">Sci-Lab</a></li>
                    <li><a href="join.html">Join Club</a></li>
                    <li><a href="wall-magazine.html">Wall Magazine</a></li>
                    <li><a href="posts.html">Posts & News</a></li>
                    <li><a href="gallery.html">Photo Gallery</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Official Contact</h4>
                <ul class="contact-info">
                    <li><i class="fa-solid fa-location-dot"></i> Dhaka College, Dhaka-1205, Bangladesh</li>
                    <li><i class="fa-solid fa-envelope"></i> official.dcsc@gmail.com</li>
                    <li><i class="fa-brands fa-instagram"></i> @dcsc_official</li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Dhaka College Science Club (DCSC). All Rights Reserved.</p>
        </div>
    </footer>

    <script src="app.js?v=5"></script>
</body>
</html>'''

with open('achievements.html', 'w', encoding='utf-8') as f:
    f.write(empty_achievements)

# 3. Update Navbar & Footer in all HTML files
html_files = glob.glob('*.html')
for file in html_files:
    if file == 'achievements.html': continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the Posts & News link
    content = content.replace('<a href="achievements.html" class="dropdown-item"><i class="fa-solid fa-bullhorn"></i> Posts & News</a>', '<a href="posts.html" class="dropdown-item"><i class="fa-solid fa-bullhorn"></i> Posts & News</a>')
    
    # Ensure footer has all quick links
    footer_old = '''                <h4>Quick Navigation</h4>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="events.html">Events</a></li>
                    <li><a href="achievements.html">Achievements</a></li>
                    <li><a href="scilab.html">Sci-Lab</a></li>
                    <li><a href="join.html">Join Club</a></li>
                </ul>'''
    footer_new = '''                <h4>Quick Navigation</h4>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="events.html">Events</a></li>
                    <li><a href="achievements.html">Achievements</a></li>
                    <li><a href="scilab.html">Sci-Lab</a></li>
                    <li><a href="join.html">Join Club</a></li>
                    <li><a href="wall-magazine.html">Wall Magazine</a></li>
                    <li><a href="posts.html">Posts & News</a></li>
                    <li><a href="gallery.html">Photo Gallery</a></li>
                </ul>'''
    content = content.replace(footer_old, footer_new)

    # Bump JS version
    content = content.replace('app.js?v=4', 'app.js?v=5')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Navbar, Footer, and Posts page updated successfully.")
