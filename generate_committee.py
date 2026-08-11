students = [
    ("Nazmus Sakib", "President", "c1.jpg"),
    ("Afnan Bhuiyan Nabil", "General Secretary", "c2.jpg"),
    ("Fahim Ahmed", "Sec of Planning and Development", "c3.jpg"),
    ("Md. Abu Kawsar Hadi", "General Coordinator", "c4.jpg"),
    ("Md. Redwan Rashid Miji", "Vice President of Administration", "c5.jpg"),
    ("Aritra Das", "Vice President of Event Management", "c6.jpg"),
    ("Al Samad Eusha", "Vice President of Sponsorship and Communication", "c7.jpg"),
    ("Muntasin Rahman Mahin", "Vice President of Publication", "c8.jpg"),
    ("Fahim Shahriar Shawn", "Vice President of Olympiad and Workshop", "c9.jpg"),
    ("Ayman Mahim Abid", "Vice President of Public Relation", "c10.jpg"),
    ("Md. Jahedur Rahman Thoha", "Assistant General Secretary", "c11.jpg"),
    ("Abdul Muhaimin Mojumder", "Assistant General Coordinator", "c12.jpg"),
    ("Md. Moin Uddin Bhuiyan Fahim", "Joint Secretary of Administration", "c13.jpg"),
    ("Abrar Bin Rashed Ayon", "Joint Secretary of Sponsorship and Communication", "c14.jpg"),
    ("Mujahidul Islam", "Joint Secretary of Publication", "c15.jpg"),
    ("Yeasin Arafat", "Joint Secretary of Public Relation", "c16.jpg"),
    ("Nazmul Alam Shanto", "Joint Secretary of IT", "c17.jpg"),
    ("SM Shahanur Rahman Sohan", "Joint Secretary of Project Development", "c18.jpg"),
    ("Mehedi Hasan", "Joint Secretary of Logistics", "c19.jpg"),
    ("Rafsun Rahman Saki", "Head of Administration", "c20.jpg"),
    ("Faiyaz Al Hadad", "Head of Event Management", "c21.jpg"),
    ("Srijon Kumar Shill", "Head of Publication", "c22.jpg"),
    ("Abdul Hai Sajim", "Head of Quiz", "c23.jpg"),
    ("Md. Shahariar Nafish", "Head of Sponsorship and Communication", "c24.jpg"),
    ("Shouvik Chanda", "Head of Olympiad and Workshop", "c25.jpg"),
    ("Mehedi Hasan Jidan", "Head of Public Relation", "c26.jpg"),
    ("Musfiq Bin Musa", "Head of IT", "c27.jpg"),
    ("Ahmed Bin Noor", "Head of Project Development", "c28.jpg"),
    ("Argho Ghosh", "Head of Logistics", "c29.jpg")
]

teachers = [
    ("Prof. Faria Sultana", "Convener", "Head of the Zoology Department", "t1.webp"),
    ("Md. Zillur Rahman", "Mentor", "Assistant Professor, Department of Botany", "t2.webp"),
    ("Afroja Nasrin", "Mentor", "Associate Professor, Department of Zoology", "t3.webp"),
    ("Bikash Kumar Das", "Mentor", "Associate Professor, Department of Chemistry", "t4.webp")
]

teachers_html = ""
for t in teachers:
    teachers_html += f'''                    <div class="team-card animate-on-scroll" style="border-top: 4px solid var(--gold-accent);">
                        <div class="team-img-wrapper">
                            <img src="image/{t[3]}" alt="{t[0]}">
                        </div>
                        <div class="team-info">
                            <h3 class="team-name" style="color:var(--gold-accent);">{t[0]}</h3>
                            <p class="team-role" style="color:var(--text-primary); font-weight:700;">{t[1]}</p>
                            <p class="team-dept" style="color:var(--text-secondary); font-size:0.85rem; margin-top:5px;">{t[2]}</p>
                        </div>
                    </div>\n'''

students_html = ""
for s in students:
    students_html += f'''                    <div class="team-card animate-on-scroll">
                        <div class="team-img-wrapper">
                            <img src="image/{s[2]}" alt="{s[0]}">
                        </div>
                        <div class="team-info">
                            <h3 class="team-name">{s[0]}</h3>
                            <p class="team-role">{s[1]}</p>
                        </div>
                    </div>\n'''

html_content = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Committee | Dhaka College Science Club</title>
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
                <a href="achievements.html" class="nav-link">Achievements</a>
                <a href="committee.html" class="nav-link active">Committee</a>
                <a href="scilab.html" class="nav-link">Sci-Lab</a>
                
                <div class="nav-dropdown">
                    <a href="#" class="nav-link dropdown-toggle">More <i class="fa-solid fa-chevron-down" style="font-size:0.75rem;"></i></a>
                    <div class="dropdown-menu">
                        <a href="wall-magazine.html" class="dropdown-item"><i class="fa-solid fa-newspaper"></i> Wall Magazine</a>
                        <a href="achievements.html" class="dropdown-item"><i class="fa-solid fa-bullhorn"></i> Posts & News</a>
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
            <h1 class="page-title">Our Leaders & Mentors</h1>
            <p class="page-subtitle">The guiding lights and dynamic minds behind DCSC</p>
        </section>

        <!-- TEACHER PANEL -->
        <section class="section-padding" style="background:rgba(255,255,255,0.02);">
            <div class="section-container">
                <div class="section-header" style="margin-bottom: 50px;">
                    <h2 class="section-title">Honorable Teacher Panel</h2>
                    <div class="title-underline"></div>
                </div>
                <div class="team-grid">
{teachers_html}
                </div>
            </div>
        </section>

        <!-- EXECUTIVE COMMITTEE -->
        <section class="section-padding">
            <div class="section-container">
                <div class="section-header" style="margin-bottom: 50px;">
                    <h2 class="section-title">Executive Committee 2025-26</h2>
                    <div class="title-underline"></div>
                    <p style="color:var(--text-secondary); max-width:600px; margin:20px auto; font-style:italic;">
                        "Leadership is unlocking people's potential to become better." — Bill Bradley
                    </p>
                </div>
                <div class="team-grid">
{students_html}
                </div>
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

    <script src="app.js?v=4"></script>
</body>
</html>
'''

with open('committee.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated committee.html")
