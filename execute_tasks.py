import os
import glob
import re

# ==============================================================
# TASK 7: REMOVE SOUND BUTTON FROM ALL HTML FILES
# ==============================================================
html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove sound button
    content = re.sub(r'<button class="icon-btn" id="sound-btn" title="Toggle Theme Song">.*?</button>\s*', '', content)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# ==============================================================
# TASK 7 (part 2): REMOVE AUDIO LOGIC FROM APP.JS
# ==============================================================
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Remove themeAudio logic
app_js = re.sub(r'// --- Multi-Path Background Audio Player ---.*?// --- Posts Database ---', '// --- Posts Database ---', app_js, flags=re.DOTALL)
app_js = re.sub(r'sound:\s*false,', '', app_js)
app_js = re.sub(r'const soundBtn\s*=\s*document\.getElementById\(\'sound-btn\'\);\s*if \(soundBtn\).*?}\s*}', '}', app_js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

# ==============================================================
# TASK 4: COMMITTEE - REMOVE TEXT, FULL SIZE IMAGES
# ==============================================================
students = [f"c{i}.jpg" for i in range(1, 30)]
teachers = [f"t{i}.webp" for i in range(1, 5)]

teachers_html = ""
for t in teachers:
    teachers_html += f'''                    <div class="team-card animate-on-scroll" style="padding:0; overflow:hidden; border: 4px solid var(--gold-accent);">
                        <img src="image/{t}" alt="Mentor" style="width:100%; height:100%; object-fit:cover; display:block;">
                    </div>\n'''

students_html = ""
for s in students:
    students_html += f'''                    <div class="team-card animate-on-scroll" style="padding:0; overflow:hidden;">
                        <img src="image/{s}" alt="Member" style="width:100%; height:100%; object-fit:cover; display:block;">
                    </div>\n'''

with open('committee.html', 'r', encoding='utf-8') as f:
    committee = f.read()

# Replace Teacher Grid
committee = re.sub(r'(<div class="section-header" style="margin-bottom: 50px;">\s*<h2 class="section-title">Honorable Teacher Panel</h2>\s*<div class="title-underline"></div>\s*</div>\s*<div class="team-grid">).*?(</div>\s*</div>\s*</section>\s*<!-- EXECUTIVE COMMITTEE -->)', r'\1\n' + teachers_html + r'                \2', committee, flags=re.DOTALL)

# Replace Student Grid
committee = re.sub(r'(<h2 class="section-title">Executive Committee 2025-26</h2>\s*<div class="title-underline"></div>\s*<p.*?</p>\s*</div>\s*<div class="team-grid">).*?(</div>\s*</div>\s*</section>\s*</main>)', r'\1\n' + students_html + r'                \2', committee, flags=re.DOTALL)

with open('committee.html', 'w', encoding='utf-8') as f:
    f.write(committee)

# ==============================================================
# TASK 3: WALL MAGAZINE MOSAIC
# ==============================================================
wonders = [f"w{i}.jpg" for i in range(1, 12)]
wonders_html = ""
for w in wonders:
    wonders_html += f'''                    <div class="animate-on-scroll" style="aspect-ratio: 1/1; overflow: hidden; width: 100%;">
                        <img src="image/{w}" alt="Wall Magazine" style="width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.4s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                    </div>\n'''

with open('wall-magazine.html', 'r', encoding='utf-8') as f:
    wall = f.read()

# Replace posts-grid with a gapless CSS grid
wall = re.sub(r'<div class="posts-grid">', '<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 0; width: 100%;">', wall)
wall = re.sub(r'(<div style="display: grid; grid-template-columns: repeat\(auto-fill, minmax\(250px, 1fr\)\); gap: 0; width: 100%;">).*?(</div>\s*</div>\s*</section>)', r'\1\n' + wonders_html + r'                \2', wall, flags=re.DOTALL)

with open('wall-magazine.html', 'w', encoding='utf-8') as f:
    f.write(wall)

# ==============================================================
# TASK 2: ACHIEVEMENTS TIMELINE
# ==============================================================
achievements_html = '''                <div class="timeline-container" style="position: relative; max-width: 800px; margin: 0 auto;">
                    <!-- Timeline Line -->
                    <div style="position: absolute; left: 50%; top: 0; bottom: 0; width: 4px; background: var(--cyan-glow); transform: translateX(-50%); box-shadow: 0 0 15px var(--cyan-glow); border-radius: 2px;"></div>
                    
                    <!-- A1 -->
                    <div class="timeline-item animate-on-scroll" style="display: flex; justify-content: flex-end; padding-right: 50%; position: relative; margin-bottom: 40px;">
                        <div style="position: absolute; right: calc(50% - 12px); top: 20px; width: 24px; height: 24px; border-radius: 50%; background: var(--gold-accent); border: 4px solid var(--bg-main); z-index: 2;"></div>
                        <div class="timeline-content" style="width: 85%; background: var(--card-bg); border-radius: 16px; padding: 25px; border: 1px solid var(--border-color); position: relative;">
                            <div style="color: var(--cyan-glow); font-weight: 700; margin-bottom: 10px;">23 November 2025</div>
                            <h3 style="color: #fff; font-size: 1.4rem; margin-bottom: 10px;">DC Nakshatra shines again!</h3>
                            <p style="color: var(--text-secondary); line-height: 1.6;">1st Runner-Up at the National Quiz Competition 2025, outperforming 120 colleges.<br><br>Huge congratulations from DCSC to Abdul Hai Sajim, Redwan Rashid and Afnan Bhuiya Nabil for this incredible achievement!</p>
                        </div>
                    </div>

                    <!-- A2 -->
                    <div class="timeline-item animate-on-scroll" style="display: flex; justify-content: flex-start; padding-left: 50%; position: relative; margin-bottom: 40px;">
                        <div style="position: absolute; left: calc(50% - 12px); top: 20px; width: 24px; height: 24px; border-radius: 50%; background: var(--gold-accent); border: 4px solid var(--bg-main); z-index: 2;"></div>
                        <div class="timeline-content" style="width: 85%; margin-left: 15%; background: var(--card-bg); border-radius: 16px; padding: 25px; border: 1px solid var(--border-color); position: relative;">
                            <div style="color: var(--cyan-glow); font-weight: 700; margin-bottom: 10px;">5 December 2025</div>
                            <h3 style="color: #fff; font-size: 1.4rem; margin-bottom: 10px;">Poster Designing Triumph</h3>
                            <p style="color: var(--text-secondary); line-height: 1.6;">We congratulate Fahim Ahmed, Sub Executive member of Dhaka College Science Club, for his incredible performance in Poster Designing across three national festivals.<br><br>He secured 2nd Runner Up at the 1st National Media Carnival (Notre Dame College), 1st Runner Up at TechNova 25 (Mohammadpur Preparatory School and College) and achieved the champion title at the 3rd Ideal Business Festival 2025 (Ideal School and College).</p>
                        </div>
                    </div>

                    <!-- A3 -->
                    <div class="timeline-item animate-on-scroll" style="display: flex; justify-content: flex-end; padding-right: 50%; position: relative; margin-bottom: 40px;">
                        <div style="position: absolute; right: calc(50% - 12px); top: 20px; width: 24px; height: 24px; border-radius: 50%; background: var(--gold-accent); border: 4px solid var(--bg-main); z-index: 2;"></div>
                        <div class="timeline-content" style="width: 85%; background: var(--card-bg); border-radius: 16px; padding: 25px; border: 1px solid var(--border-color); position: relative;">
                            <div style="color: var(--cyan-glow); font-weight: 700; margin-bottom: 10px;">24 October 2025</div>
                            <h3 style="color: #fff; font-size: 1.4rem; margin-bottom: 10px;">5th Gregorian National Knowledge Fiesta</h3>
                            <p style="color: var(--text-secondary); line-height: 1.6;">Congratulations to Mohammad Saidur Rahman of DC Lubdhak on his outstanding performance: Champion in Anime Quiz and What If?, 1st Runner-up in Movie Quiz and IT Quiz, and 2nd Runner-up in Solo Quiz.<br><br>The DCSC family wholeheartedly applauds his dedication and brilliance.</p>
                        </div>
                    </div>

                    <!-- A4 -->
                    <div class="timeline-item animate-on-scroll" style="display: flex; justify-content: flex-start; padding-left: 50%; position: relative; margin-bottom: 40px;">
                        <div style="position: absolute; left: calc(50% - 12px); top: 20px; width: 24px; height: 24px; border-radius: 50%; background: var(--gold-accent); border: 4px solid var(--bg-main); z-index: 2;"></div>
                        <div class="timeline-content" style="width: 85%; margin-left: 15%; background: var(--card-bg); border-radius: 16px; padding: 25px; border: 1px solid var(--border-color); position: relative;">
                            <div style="color: var(--cyan-glow); font-weight: 700; margin-bottom: 10px;">October 2025</div>
                            <h3 style="color: #fff; font-size: 1.4rem; margin-bottom: 10px;">National Math Summit Champion</h3>
                            <p style="color: var(--text-secondary); line-height: 1.6;">We are delighted to announce that Azmain Islam, a member of the Dhaka College Science Club(DCSC), has secured 1st place in the Math Olympiad (Higher Secondary Category) at the 2nd DRMC National Math Summit.<br><br>We warmly congratulate Azmain on this success and encourage him to continue pursuing excellence.</p>
                        </div>
                    </div>
                    
                    <!-- A5 -->
                    <div class="timeline-item animate-on-scroll" style="display: flex; justify-content: flex-end; padding-right: 50%; position: relative; margin-bottom: 40px;">
                        <div style="position: absolute; right: calc(50% - 12px); top: 20px; width: 24px; height: 24px; border-radius: 50%; background: var(--gold-accent); border: 4px solid var(--bg-main); z-index: 2;"></div>
                        <div class="timeline-content" style="width: 85%; background: var(--card-bg); border-radius: 16px; padding: 25px; border: 1px solid var(--border-color); position: relative;">
                            <div style="color: var(--cyan-glow); font-weight: 700; margin-bottom: 10px;">13 October 2025</div>
                            <h3 style="color: #fff; font-size: 1.4rem; margin-bottom: 10px;">MGCSC Mindspark Science Expo</h3>
                            <p style="color: var(--text-secondary); line-height: 1.6;">Dhaka College Science Club’s Project Display Team DC Niharika has proudly secured the Champion title in the Project Display (Senior Category) at the 3rd MGCSC Mindspark Science Expo 2025!<br><br>Their groundbreaking project, “FloodRover,” stands as a testament to the team’s unwavering dedication. Congratulations to Protyoy Nandi and Md. Abu Kawsar Hadi!</p>
                        </div>
                    </div>
                </div>
                <style>
                    @media (max-width: 768px) {
                        .timeline-container > div:first-child { left: 20px !important; }
                        .timeline-item { justify-content: flex-start !important; padding-right: 0 !important; padding-left: 50px !important; }
                        .timeline-item > div:nth-child(1) { left: 8px !important; right: auto !important; }
                        .timeline-content { width: 100% !important; margin-left: 0 !important; }
                    }
                </style>
'''

with open('achievements.html', 'r', encoding='utf-8') as f:
    ach = f.read()

ach = re.sub(r'<div class="section-container" style="text-align: center; min-height: 40vh; display: flex; flex-direction: column; justify-content: center; align-items: center;">.*?</div>', achievements_html, ach, flags=re.DOTALL)
with open('achievements.html', 'w', encoding='utf-8') as f:
    f.write(ach)

print("Tasks 2, 3, 4, 7 completed successfully.")
