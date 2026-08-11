import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The HTML to insert for the preview sections
preview_html = """
        <!-- PREVIEW SECTIONS: ACHIEVEMENTS -->
        <section class="section-padding">
            <div class="section-container">
                <div class="section-header">
                    <span class="section-subtitle">OUR PRIDE</span>
                    <h2 class="section-title">Latest Achievements</h2>
                    <div class="title-bar"></div>
                </div>
                <div class="timeline" style="margin-top: 30px;">
                    <div class="timeline-item animate-on-scroll">
                        <div class="timeline-dot"></div>
                        <div class="timeline-content">
                            <h3 style="color: var(--cyan-glow); margin-bottom: 10px; font-size: 1.5rem;">DC Nakshatra shines again!</h3>
                            <div class="timeline-date" style="color: var(--text-secondary); margin-bottom: 15px; font-weight: 600;">23 November 2025</div>
                            <p>1st Runner-Up at the National Quiz Competition 2025, outperforming 120 colleges. Huge congratulations from DCSC to Abdul Hai Sajim, Redwan Rashid and Afnan Bhuiya Nabil!</p>
                        </div>
                    </div>
                </div>
                <div style="text-align: center; margin-top: 40px;">
                    <a href="achievements.html" class="btn-primary" style="padding: 12px 30px; font-size: 1.1rem;">See All Achievements <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i></a>
                </div>
            </div>
        </section>

        <!-- PREVIEW SECTIONS: EVENTS -->
        <section class="section-padding bg-alt">
            <div class="section-container">
                <div class="section-header">
                    <span class="section-subtitle">UPCOMING & RECENT</span>
                    <h2 class="section-title">Events & Festivals</h2>
                    <div class="title-bar"></div>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 30px;">
                    <div class="event-card animate-on-scroll" style="background: var(--card-bg); border-radius: 16px; overflow: hidden; border: 1px solid var(--border-color);">
                        <div style="height: 200px; overflow: hidden;">
                            <img src="image/E1.jpg" alt="AI NeuroVerse" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <div style="padding: 25px;">
                            <h3 style="color: #fff; margin-bottom: 15px; font-size: 1.3rem;">DCSC AI NeuroVerse 2026</h3>
                            <p style="color: var(--text-secondary); margin-bottom: 20px;">The biggest AI fest of the year showcasing neural networks and robotics.</p>
                            <a href="event-neuroverse.html" style="color: var(--cyan-glow); text-decoration: none; font-weight: 600;">Read More <i class="fa-solid fa-arrow-right"></i></a>
                        </div>
                    </div>
                    <div class="event-card animate-on-scroll" style="background: var(--card-bg); border-radius: 16px; overflow: hidden; border: 1px solid var(--border-color);">
                        <div style="height: 200px; overflow: hidden;">
                            <img src="image/E4.png" alt="Quizzing" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <div style="padding: 25px;">
                            <h3 style="color: #fff; margin-bottom: 15px; font-size: 1.3rem;">Everything About Quizzing</h3>
                            <p style="color: var(--text-secondary); margin-bottom: 20px;">A detailed workshop on how to excel at national level quiz competitions.</p>
                            <a href="event-quizzing.html" style="color: var(--cyan-glow); text-decoration: none; font-weight: 600;">Read More <i class="fa-solid fa-arrow-right"></i></a>
                        </div>
                    </div>
                </div>
                <div style="text-align: center; margin-top: 40px;">
                    <a href="events.html" class="btn-primary" style="padding: 12px 30px; font-size: 1.1rem;">Explore All Events <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i></a>
                </div>
            </div>
        </section>

        <!-- PREVIEW SECTIONS: WALL MAGAZINE -->
        <section class="section-padding">
            <div class="section-container">
                <div class="section-header">
                    <span class="section-subtitle">SCIENCE ARTICLES</span>
                    <h2 class="section-title">Wednesday Wonders</h2>
                    <div class="title-bar"></div>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 0; border-radius: 20px; overflow: hidden; margin-top: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1);">
                    <div style="aspect-ratio: 1/1; overflow: hidden;">
                        <img src="image/W1.jpg" alt="Wall Magazine" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    </div>
                    <div style="aspect-ratio: 1/1; overflow: hidden;">
                        <img src="image/W2.jpg" alt="Wall Magazine" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    </div>
                    <div style="aspect-ratio: 1/1; overflow: hidden;">
                        <img src="image/W3.jpg" alt="Wall Magazine" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                    </div>
                </div>
                <div style="text-align: center; margin-top: 40px;">
                    <a href="wall-magazine.html" class="btn-primary" style="padding: 12px 30px; font-size: 1.1rem;">Read Full Magazine <i class="fa-solid fa-arrow-right" style="margin-left: 8px;"></i></a>
                </div>
            </div>
        </section>

"""

if 'PREVIEW SECTIONS' not in content:
    # Insert right before Google Maps Embed Section
    content = content.replace('<!-- GOOGLE MAPS EMBED SECTION -->', preview_html + '\n        <!-- GOOGLE MAPS EMBED SECTION -->')
    
    # Also update cache buster just in case
    content = content.replace('v=7', 'v=8')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully added previews to index.html")
else:
    print("Previews already added to index.html")
