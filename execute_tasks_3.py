import re

# ==============================================================
# TASK 6: POST IMAGE CAROUSEL & ADD P11
# ==============================================================
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Add Post 11 data
p11_data = '''    11: {
        title: "Intra Science Festival & Freshers' Orientation 2025",
        date: "12 December 2025",
        tag: "Festival",
        images: ["image/p11.1.jpg", "image/e11.2.jpg", "image/e11.3.jpg", "image/e11.4.jpg"],
        body: `Dhaka College Science Club successfully hosted DCSC presents "Intra Science Festival & Freshers' Orientation 2025" from 11–13 November. 

Here are some highlights from Day 1 of the event , including glimpses from all the segments.`
    },
'''
app_js = re.sub(r'(const postsData = {)', r'\1\n' + p11_data, app_js)

# Update openPostModal
modal_js = '''
let currentPostImages = [];
let currentImageIndex = 0;

function openPostModal(id) {
    const post = postsData[id];
    if (!post) return;

    const modalArea = document.getElementById('modal-content-area');
    const modal = document.getElementById('post-modal');

    currentPostImages = post.images || [];
    currentImageIndex = 0;

    let imagesHTML = '';
    if (currentPostImages.length > 0) {
        imagesHTML = `
            <div style="position:relative; width:100%; height:300px; border-radius:12px; overflow:hidden; margin-bottom:20px; border:1px solid var(--border-color); background:#000;">
                <img id="post-carousel-img" src="${currentPostImages[0]}" style="width:100%; height:100%; object-fit:contain;">
                ${currentPostImages.length > 1 ? `
                    <button onclick="prevPostImage()" style="position:absolute; left:10px; top:50%; transform:translateY(-50%); background:rgba(0,0,0,0.7); color:#fff; border:none; width:40px; height:40px; border-radius:50%; cursor:pointer; z-index:10; font-size:1.2rem;"><i class="fa-solid fa-chevron-left"></i></button>
                    <button onclick="nextPostImage()" style="position:absolute; right:10px; top:50%; transform:translateY(-50%); background:rgba(0,0,0,0.7); color:#fff; border:none; width:40px; height:40px; border-radius:50%; cursor:pointer; z-index:10; font-size:1.2rem;"><i class="fa-solid fa-chevron-right"></i></button>
                    <div id="post-carousel-indicator" style="position:absolute; bottom:10px; left:50%; transform:translateX(-50%); background:rgba(0,0,0,0.7); color:#fff; padding:4px 10px; border-radius:12px; font-size:0.8rem;">1 / ${currentPostImages.length}</div>
                ` : ''}
            </div>
        `;
    }

    modalArea.innerHTML = `
        <div style="margin-bottom:12px;">
            <span style="color:var(--cyan-glow); font-weight:700; font-size:0.85rem;">${post.tag}</span> | 
            <span style="color:var(--text-muted); font-size:0.85rem;"><i class="fa-regular fa-calendar"></i> ${post.date}</span>
        </div>
        <h2 style="font-family:var(--font-heading); font-size:1.6rem; margin-bottom:20px; color:var(--text-primary); text-transform:none;">${post.title}</h2>
        ${imagesHTML}
        <div style="color:var(--text-secondary); font-size:1rem; line-height:1.8; white-space:pre-line;">
            ${post.body}
        </div>
    `;

    modal.classList.add('active');
}

function nextPostImage() {
    if(currentPostImages.length <= 1) return;
    currentImageIndex = (currentImageIndex + 1) % currentPostImages.length;
    updateCarousel();
}

function prevPostImage() {
    if(currentPostImages.length <= 1) return;
    currentImageIndex = (currentImageIndex - 1 + currentPostImages.length) % currentPostImages.length;
    updateCarousel();
}

function updateCarousel() {
    document.getElementById('post-carousel-img').src = currentPostImages[currentImageIndex];
    document.getElementById('post-carousel-indicator').innerText = (currentImageIndex + 1) + " / " + currentPostImages.length;
}

function closePostModal() {
    const modal = document.getElementById('post-modal');
    if (modal) modal.classList.remove('active');
}
'''
app_js = re.sub(r'function openPostModal\(id\).*?function closePostModal\(\)\s*\{.*?\}', modal_js, app_js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

# ==============================================================
# TASK 5: EVENTS HTML RE-WRITE
# ==============================================================
events_html = '''
        <!-- EVENTS SECTION -->
        <section class="section-padding">
            <div class="section-container">
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
                    
                    <!-- E6: Freshers Orientation -->
                    <div class="event-showcase-card animate-on-scroll landscape">
                        <img src="image/e6.jpg" alt="Freshers Orientation">
                        <div class="event-content">
                            <div class="event-date">Upcoming</div>
                            <h3 class="event-title">Intra Science Festival & Freshers' Orientation 2025</h3>
                            <div class="event-meta">
                                <span><i class="fa-solid fa-location-dot"></i> Dhaka College</span>
                            </div>
                            <a href="event-freshers.html" class="btn-primary" style="margin-top: 20px; display: inline-block;">View Details</a>
                        </div>
                    </div>

                    <!-- E4: Quizzing -->
                    <div class="event-showcase-card animate-on-scroll landscape">
                        <img src="image/e4.jpg" alt="Quizzing Session">
                        <div class="event-content">
                            <div class="event-date">11 December 2025</div>
                            <h3 class="event-title">Everything About Quizzing</h3>
                            <div class="event-meta">
                                <span><i class="fa-solid fa-location-dot"></i> Khurram Auditorium</span>
                            </div>
                            <a href="event-quizzing.html" class="btn-primary" style="margin-top: 20px; display: inline-block;">View Details</a>
                        </div>
                    </div>

                    <!-- E5: US Study -->
                    <div class="event-showcase-card animate-on-scroll square">
                        <img src="image/e5.jpg" alt="Study in US">
                        <div class="event-content">
                            <div class="event-date">15 November 2025</div>
                            <h3 class="event-title">Studying in the U.S.</h3>
                            <div class="event-meta">
                                <span><i class="fa-solid fa-location-dot"></i> Online / DCSC</span>
                            </div>
                            <a href="event-us.html" class="btn-primary" style="margin-top: 20px; display: inline-block;">View Details</a>
                        </div>
                    </div>

                    <!-- E1: NeuroVerse -->
                    <div class="event-showcase-card animate-on-scroll square">
                        <img src="image/e1.jpg" alt="NeuroVerse">
                        <div class="event-content">
                            <div class="event-date">12 October 2026</div>
                            <h3 class="event-title">DCSC AI NeuroVerse 2026</h3>
                            <div class="event-meta">
                                <span><i class="fa-solid fa-location-dot"></i> Dhaka College</span>
                            </div>
                            <a href="event-neuroverse.html" class="btn-primary" style="margin-top: 20px; display: inline-block;">View Details</a>
                        </div>
                    </div>

                </div>

            </div>
        </section>
'''

with open('events.html', 'r', encoding='utf-8') as f:
    ev = f.read()

ev = re.sub(r'<!-- MAJOR EVENT: AI NEUROVERSE -->.*?(</main>)', events_html + r'\n\1', ev, flags=re.DOTALL)
with open('events.html', 'w', encoding='utf-8') as f:
    f.write(ev)

print("Tasks 5 (events.html) and 6 (app.js) completed.")
