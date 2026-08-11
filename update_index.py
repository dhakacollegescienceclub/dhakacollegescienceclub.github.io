import re

new_sections = '''
        <!-- FEATURED POSTS & NEWS -->
        <section class="section-padding bg-alt">
            <div class="section-container">
                <div class="section-header" style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 15px;">
                    <div>
                        <span class="section-subtitle">UPDATES</span>
                        <h2 class="section-title">Recent Posts & News</h2>
                        <div class="title-bar"></div>
                    </div>
                    <a href="posts.html" class="btn-primary" style="padding: 10px 20px; font-size: 0.9rem;">View All Posts <i class="fa-solid fa-arrow-right"></i></a>
                </div>

                <div class="posts-grid">
                    <div class="post-card animate-on-scroll">
                        <div class="post-media">
                            <img src="image/p1.jpg" alt="July Mass Uprising Memorial" class="post-img">
                        </div>
                        <div class="post-body">
                            <div style="font-size:0.8rem; color:var(--cyan-glow); font-weight:700; margin-bottom:6px;">Memorial</div>
                            <h3 class="post-title">July Mass Uprising Memorial</h3>
                            <p style="color:var(--text-secondary); font-size:0.9rem; margin-bottom:16px;">July is not just a month — it is a symbol of courage, sacrifice, and change.</p>
                            <button class="btn-primary" onclick="openPostModal(1)">Read Full Story</button>
                        </div>
                    </div>

                    <div class="post-card animate-on-scroll">
                        <div class="post-media">
                            <img src="image/p2.1.jpg" alt="Olympiad Hunt 4.0 Prize Giving Ceremony" class="post-img">
                        </div>
                        <div class="post-body">
                            <div style="font-size:0.8rem; color:var(--cyan-glow); font-weight:700; margin-bottom:6px;">Prize Giving</div>
                            <h3 class="post-title">Olympiad Hunt 4.0 Prize Giving Ceremony</h3>
                            <p style="color:var(--text-secondary); font-size:0.9rem; margin-bottom:16px;">Dhaka College Science Club is pleased to reveal the vibrant Prize Giving Ceremony of Olympiad Hunt 4.0!</p>
                            <button class="btn-primary" onclick="openPostModal(2)">Read Full Story</button>
                        </div>
                    </div>

                    <div class="post-card animate-on-scroll">
                        <div class="post-media">
                            <img src="image/p3.1.jpg" alt="Olympiad Hunt - Talent Hunt 2026" class="post-img">
                        </div>
                        <div class="post-body">
                            <div style="font-size:0.8rem; color:var(--cyan-glow); font-weight:700; margin-bottom:6px;">Olympiad</div>
                            <h3 class="post-title">Olympiad Hunt - Talent Hunt 2026</h3>
                            <p style="color:var(--text-secondary); font-size:0.9rem; margin-bottom:16px;">Olympiad Hunt: A day full of learning, excitement, and healthy competition.</p>
                            <button class="btn-primary" onclick="openPostModal(3)">Read Full Story</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- UPCOMING EVENTS PREVIEW -->
        <section class="section-padding">
            <div class="section-container">
                <div class="section-header" style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 15px;">
                    <div>
                        <span class="section-subtitle">HAPPENINGS</span>
                        <h2 class="section-title">Events & Festivals</h2>
                        <div class="title-bar"></div>
                    </div>
                    <a href="events.html" class="btn-primary" style="padding: 10px 20px; font-size: 0.9rem;">View All Events <i class="fa-solid fa-arrow-right"></i></a>
                </div>

                <div class="event-showcase-card animate-on-scroll">
                    <div class="event-image-box">
                        <img src="image/e1.jpg" alt="DCSC AI NeuroVerse 2026">
                        <div class="event-date-badge">14<br>MAY</div>
                    </div>
                    <div class="event-content-box">
                        <div class="event-tags">
                            <span class="tag">AI</span>
                            <span class="tag">Mega Event</span>
                        </div>
                        <h3 class="event-title">DCSC AI NeuroVerse 2026</h3>
                        <p class="event-desc">Are you ready to unlock the true potential of AI? DCSC brings you the biggest Artificial Intelligence festival of the year! From hands-on workshops to intense hackathons, AI NeuroVerse is the ultimate playground for future tech leaders.</p>
                        <a href="events.html" class="btn-primary" style="margin-top: 20px; width: fit-content;">See Details</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- WALL MAGAZINE PREVIEW -->
        <section class="section-padding bg-alt">
            <div class="section-container">
                <div class="section-header" style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 15px;">
                    <div>
                        <span class="section-subtitle">KNOWLEDGE HUB</span>
                        <h2 class="section-title">Wednesday Wonders</h2>
                        <div class="title-bar"></div>
                    </div>
                    <a href="wall-magazine.html" class="btn-primary" style="padding: 10px 20px; font-size: 0.9rem;">Read All Articles <i class="fa-solid fa-arrow-right"></i></a>
                </div>

                <div class="posts-grid">
                    <div class="wonder-card animate-on-scroll">
                        <div class="wonder-img-box">
                            <img src="image/w1.jpg" alt="Time Crystal" class="wonder-img">
                            <div class="wonder-tag">Physics</div>
                        </div>
                        <div class="wonder-content">
                            <div class="wonder-date">5 August 2026</div>
                            <h3 class="wonder-title">Time Crystal</h3>
                            <p class="wonder-excerpt">Does the name "Time Crystal" make you curious? Well there's a unique state of matter called Time Crystal where matter repeats its structure in time...</p>
                        </div>
                    </div>

                    <div class="wonder-card animate-on-scroll">
                        <div class="wonder-img-box">
                            <img src="image/w2.jpg" alt="Hemophobia" class="wonder-img">
                            <div class="wonder-tag">Biology</div>
                        </div>
                        <div class="wonder-content">
                            <div class="wonder-date">29 July 2026</div>
                            <h3 class="wonder-title">The Science of Hemophobia</h3>
                            <p class="wonder-excerpt">Blood is vital for life, but for some people, just seeing it can cause them to feel faint in seconds. Why does seeing blood cause the brain to shut down?</p>
                        </div>
                    </div>

                    <div class="wonder-card animate-on-scroll">
                        <div class="wonder-img-box">
                            <img src="image/w3.jpg" alt="ISS" class="wonder-img">
                            <div class="wonder-tag">Astronomy</div>
                        </div>
                        <div class="wonder-content">
                            <div class="wonder-date">July 2026</div>
                            <h3 class="wonder-title">International Space Station</h3>
                            <p class="wonder-excerpt">Do you know what the largest human-made structure in space is? It is the International Space Station, orbiting Earth at roughly 400 km altitude.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- COMMITTEE LEADERS PREVIEW -->
        <section class="section-padding">
            <div class="section-container">
                <div class="section-header" style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 15px;">
                    <div>
                        <span class="section-subtitle">LEADERSHIP</span>
                        <h2 class="section-title">Our Mentors & Leaders</h2>
                        <div class="title-bar"></div>
                    </div>
                    <a href="committee.html" class="btn-primary" style="padding: 10px 20px; font-size: 0.9rem;">View Full Committee <i class="fa-solid fa-arrow-right"></i></a>
                </div>

                <div class="team-grid">
                    <div class="team-card animate-on-scroll" style="border-top: 4px solid var(--gold-accent);">
                        <div class="team-img-wrapper"><img src="image/t1.webp" alt="Prof. Faria Sultana"></div>
                        <div class="team-info">
                            <h3 class="team-name" style="color:var(--gold-accent);">Prof. Faria Sultana</h3>
                            <p class="team-role" style="color:var(--text-primary); font-weight:700;">Convener</p>
                        </div>
                    </div>
                    <div class="team-card animate-on-scroll">
                        <div class="team-img-wrapper"><img src="image/c1.jpg" alt="Nazmus Sakib"></div>
                        <div class="team-info">
                            <h3 class="team-name">Nazmus Sakib</h3>
                            <p class="team-role">President</p>
                        </div>
                    </div>
                    <div class="team-card animate-on-scroll">
                        <div class="team-img-wrapper"><img src="image/c2.jpg" alt="Afnan Bhuiyan Nabil"></div>
                        <div class="team-info">
                            <h3 class="team-name">Afnan Bhuiyan Nabil</h3>
                            <p class="team-role">General Secretary</p>
                        </div>
                    </div>
                    <div class="team-card animate-on-scroll">
                        <div class="team-img-wrapper"><img src="image/c4.jpg" alt="Md. Abu Kawsar Hadi"></div>
                        <div class="team-info">
                            <h3 class="team-name">Md. Abu Kawsar Hadi</h3>
                            <p class="team-role">General Coordinator</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- GOOGLE MAPS EMBED SECTION -->
        <section class="section-padding bg-alt">
            <div class="section-container">
                <div class="section-header">
                    <span class="section-subtitle">LOCATION & MAP</span>
                    <h2 class="section-title">Find Dhaka College Science Club</h2>
                    <div class="title-bar"></div>
                </div>
                <div style="border-radius:20px; overflow:hidden; border:1px solid var(--cyan-glow); box-shadow:0 0 30px rgba(0, 242, 254, 0.25);">
                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3652.27028249622!2d90.38466637604473!3d23.73774898926079!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3755b8c7a6597a73%3A0xc3b8602b9386d634!2sDhaka%20College!5e0!3m2!1sen!2sbd!4v1700000000000!5m2!1sen!2sbd" width="100%" height="420" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                </div>
            </div>
        </section>
'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace everything from "<!-- FEATURED SPOTLIGHT -->" to "</main>"
content = re.sub(r'<!-- FEATURED SPOTLIGHT -->.*?(</main>)', new_sections + r'\1', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated successfully with previews.")
