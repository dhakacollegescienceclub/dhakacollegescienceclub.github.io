/* ==========================================================================
   DHAKA COLLEGE SCIENCE CLUB (DCSC) - SHARED ENGINE & SILENT AUDIO PLAYER
   ========================================================================== */

// --- Global App State ---
const state = {
    theme: localStorage.getItem('dcsc_theme') || 'dark',
    
    selectedElements: [],
    quizScore: 0,
    currentQuizIndex: 0
};

// --- Posts Database ---
const postsData = {
    11: {
        title: "Intra Science Festival & Freshers' Orientation 2025",
        date: "12 December 2025",
        tag: "Festival",
        images: ["image/p11.1.jpg", "image/e11.2.jpg", "image/e11.3.jpg", "image/e11.4.jpg"],
        body: `Dhaka College Science Club successfully hosted DCSC presents "Intra Science Festival & Freshers' Orientation 2025" from 11–13 November. 

Here are some highlights from Day 1 of the event , including glimpses from all the segments.`
    },

    1: {
        title: "July Mass Uprising Memorial",
        date: "5 August 2026",
        tag: "Memorial",
        images: ["image/p1.jpg"],
        body: `July is not just a month — it is a symbol of courage, sacrifice, and change. Dhaka College Science Club pays humble respect to all the martyrs and brave participants of the July mass uprising. Everyone hopes July lives on in memory and consciousness.`
    },
    2: {
        title: "Olympiad Hunt 4.0 Prize Giving Ceremony",
        date: "25 June 2026",
        tag: "Prize Giving",
        images: ["image/p2.1.jpg", "image/p2.2.jpg", "image/p2.3.jpg", "image/p2.4.jpg"],
        body: `Dhaka College Science Club is pleased to reveal the vibrant Prize Giving Ceremony of Olympiad Hunt 4.0! It was a day of joy, applause and celebration as champions were hailed for their brilliance and remarkable achievements. Cheers, bright smiles, moments never to be forgotten echoed through the hall. The ceremony marked a perfect finale relive the excitement and festive spirit through these snapshots of an extraordinary day!`
    },
    3: {
        title: "Olympiad Hunt - Talent Hunt 2026",
        date: "19 June 2026",
        tag: "Olympiad",
        images: ["image/p3.1.jpg", "image/p3.2.jpg", "image/p3.3.jpg"],
        body: `Olympiad Hunt: A day full of learning, excitement, and healthy competition where talented students showed their knowledge and skills with confidence.\n\nThe second day of DCSC Talent Hunt 2026, organized by Dhaka College Science Club, was successfully held with the exciting segment, Olympiad Hunt. Students participated with great enthusiasm and confidence to test their knowledge, creativity, and problem-solving abilities. Their active participation and dedication made the day enjoyable and memorable for everyone.`
    },
    4: {
        title: "DCSC Talent Hunt Inauguration",
        date: "16 June 2026",
        tag: "Talent Hunt",
        images: ["image/p4.1.jpg", "image/p4.2.jpg", "image/p4.3.jpg"],
        body: `The long awaited moment has finally arrived, the DCSC Talent Hunt has been officially inaugurated!\n\nOn the very first day, the written round of the Quiz Team Selection was conducted, giving our talented members the perfect stage to put their knowledge to the test. Alongside that, the Project Development Team Selection got underway as well, with both the written round and the thesis round being held on the same day with the selected candidates.\n\nIt was a day filled with talent, hard work, and great energy. DCSC Talent Hunt is off to a wonderful start, and we look forward to the exciting days ahead!`
    },
    5: {
        title: "Eid-ul-Adha Mubarak",
        date: "17 May 2026",
        tag: "Greetings",
        images: ["image/p5.jpg"],
        body: `Eid-ul-Adha reminds us that true Qurbani is not measured by flesh or blood, but by the purity of our intentions and the depth of our taqwa. May this blessed occasion bring peace, happiness, and endless blessings to everyone.\n\nWishing a blessed Eid Mubarak to everyone from Dhaka College Science Club (DCSC)`
    },
    6: {
        title: "Condemnation of Cruelty",
        date: "24 May 2026",
        tag: "Statement",
        images: ["image/p6.jpg"],
        body: `Even as we claim to be superior as a nation, the harsh truth is proven by these images of cruelty. How deep in darkness must a society sink to accept such brutality? Those who impose barbarity on innocent lives are enemies of civilization. On behalf of Dhaka College Science Club, we strongly condemn this cruelty.`
    },
    7: {
        title: "New Sub-Executive Committee Welcome",
        date: "Committee Announcement",
        tag: "Announcement",
        images: ["image/p7.jpg"],
        body: `"The strength of the team is each individual member. The strength of each member is the team."\n\nIt is a great moment for Dhaka College Science Club (DCSC) as we reveal our newly chosen Sub-Executive Committee members. Each of them has shown true dedication and a real desire to contribute. It is a great joy to have them on board.\n\nCongratulations to all our new Sub-Executive Committee members. Your passion brought you here and we know you have something special to offer. We look forward to the positive change you will bring to Dhaka College Science Club (DCSC). We wish you growth, confidence and a journey you will remember. Welcome to the team!`
    },
    8: {
        title: "Wednesday Wonders: Ramadan Specials 2026",
        date: "17 May 2026",
        tag: "Ramadan Specials",
        images: ["image/p8.jpg"],
        body: `Wednesday Wonders Ramadan Specials 2026 successfully combined science with religion in perfect harmony.\n\nThe series covered a range of topics, including the metabolic benefits of fasting, the ethical considerations in bioengineering, the calming effects of circadian rhythms during Salah, and the divine purpose of Earth's day-and-night cycle. These four Wednesday Wonders helped us explore the relationship between science and Islam, deepening our understanding and strengthening our belief.`
    },
    9: {
        title: "Grand Iftar Mahfil",
        date: "11 March 2026",
        tag: "Iftar Mahfil",
        images: ["image/p9.1.jpg", "image/p9.2.jpg", "image/p9.3.jpg", "image/p9.4.jpg"],
        body: `The Dhaka College Science Club family came together for a warm and memorable Iftar Mahfil on March 7, 2026 (Saturday), at Brewed Harmony Intercontinental, Dhanmondi. \n\nThe evening was filled with joy, as alumni from different fields came together with the EC members, meeting old friends again and making new connections in one place. DCSC sincerely appreciates everyone who took the time to join the gathering and make the event truly special and looks forward to welcoming everyone again in future gatherings.`
    },
    10: {
        title: "Happy New Year 2026",
        date: "1 January 2026",
        tag: "Greetings",
        images: ["image/p10.jpg"],
        body: `Happy 2026!\n\n2025, the previous year was of mixed emotions, bringing both happiness and lessons. But through the tough times, Dhaka College Science Club remained a source of inspiration by organizing creative programs that brought us together. Let’s review the notable moments from the past year. Dhaka College Science Club wishes you a year ahead filled with joy and peace.`
    }
};

// --- DOM Initializer ---
document.addEventListener('DOMContentLoaded', () => {
    initCanvasParticles();
    initCustomCursor();
    initNavigation();
    initTheme();
    highlightActivePageNav();
    initScrollAnimations();
    initStatCounters();
    
    if (document.getElementById('reset-lab-btn')) initSciLab();
    if (document.getElementById('join-form')) initJoinForm();
    if (document.getElementById('cert-form')) initCertForm();
    if (document.getElementById('quiz-box')) loadQuizQuestion();
    if (document.getElementById('orbit-canvas')) initPhysicsOrbitSandbox();
});

// --- Scroll Reveal Animations ---
function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show'); entry.target.classList.add('animated');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.animate-on-scroll, .about-card, .post-card, .advisor-card, .ec-card, .segment-card, .wing-card, .stat-card, .team-card, .wonder-card, .event-showcase-card').forEach(el => {
        el.classList.add('animate-on-scroll');
        observer.observe(el);
    });
}

// --- Stats Counter Animation ---
function initStatCounters() {
    const counters = document.querySelectorAll('.stat-number[data-target]');
    if (!counters.length) return;
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.dataset.counted) {
                entry.target.dataset.counted = 'true';
                const target = parseInt(entry.target.dataset.target, 10);
                const suffix = entry.target.dataset.suffix || '';
                const duration = 1800;
                const step = Math.ceil(duration / target);
                let current = 0;
                const timer = setInterval(() => {
                    current += Math.max(1, Math.floor(target / 60));
                    if (current >= target) {
                        current = target;
                        clearInterval(timer);
                    }
                    entry.target.textContent = current + suffix;
                }, step);
            }
        });
    }, { threshold: 0.3 });
    counters.forEach(el => { el.textContent = '0'; counterObserver.observe(el); });
}


// --- Highlight Active Page ---
function highlightActivePageNav() {
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-link, .dropdown-item').forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || (currentPath === '' && href === 'index.html')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

// --- MOUSE ATTRACTING CANVAS CONSTELLATION NETWORK ---
function initCanvasParticles() {
    const canvas = document.getElementById('bg-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;
    
    window.addEventListener('resize', () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    });

    const particles = [];
    const particleCount = Math.min(Math.floor(width / 14), 85);

    for (let i = 0; i < particleCount; i++) {
        particles.push({
            x: Math.random() * width,
            y: Math.random() * height,
            vx: (Math.random() - 0.5) * 0.8,
            vy: (Math.random() - 0.5) * 0.8,
            radius: Math.random() * 2.5 + 1
        });
    }

    let mouse = { x: null, y: null };
    window.addEventListener('mousemove', (e) => {
        mouse.x = e.clientX;
        mouse.y = e.clientY;
    });
    window.addEventListener('mouseleave', () => {
        mouse.x = null;
        mouse.y = null;
    });

    function animate() {
        ctx.clearRect(0, 0, width, height);
        const isDark = state.theme === 'dark';
        const pColor = isDark ? 'rgba(0, 242, 254, 0.7)' : 'rgba(0, 82, 212, 0.5)';
        const lColor = isDark ? 'rgba(0, 242, 254, ' : 'rgba(0, 82, 212, ';

        for (let i = 0; i < particles.length; i++) {
            let p = particles[i];
            p.x += p.vx;
            p.y += p.vy;

            if (p.x < 0 || p.x > width) p.vx *= -1;
            if (p.y < 0 || p.y > height) p.vy *= -1;

            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fillStyle = pColor;
            ctx.fill();

            for (let j = i + 1; j < particles.length; j++) {
                let p2 = particles[j];
                let dist = Math.hypot(p.x - p2.x, p.y - p2.y);
                if (dist < 125) {
                    ctx.beginPath();
                    ctx.moveTo(p.x, p.y);
                    ctx.lineTo(p2.x, p2.y);
                    ctx.strokeStyle = lColor + (1 - dist / 125) * 0.22 + ')';
                    ctx.stroke();
                }
            }

            if (mouse.x !== null && mouse.y !== null) {
                let mDist = Math.hypot(p.x - mouse.x, p.y - mouse.y);
                if (mDist < 170) {
                    p.x += (mouse.x - p.x) * 0.015;
                    p.y += (mouse.y - p.y) * 0.015;

                    ctx.beginPath();
                    ctx.moveTo(p.x, p.y);
                    ctx.lineTo(mouse.x, mouse.y);
                    ctx.strokeStyle = lColor + (1 - mDist / 170) * 0.5 + ')';
                    ctx.lineWidth = 1.2;
                    ctx.stroke();
                }
            }
        }
        requestAnimationFrame(animate);
    }
    animate();
}

// --- Custom Cursor Glow ---
function initCustomCursor() {
    const cursor = document.getElementById('cursor-glow');
    if (cursor) {
        window.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });
    }
}

// --- SILENT AUDIO & NAVIGATION CONTROLS ---
function initNavigation() {
    const soundBtn = document.getElementById('sound-btn');
    const themeBtn = document.getElementById('theme-btn');

    if (soundBtn) {
        soundBtn.addEventListener('click', () => {
            state.sound = !state.sound;
            if (state.sound) {
                themeAudio.play().catch(e => console.log("Audio play error:", e));
                soundBtn.innerHTML = '<i class="fa-solid fa-volume-high"></i>';
            } else {
                themeAudio.pause();
                soundBtn.innerHTML = '<i class="fa-solid fa-volume-xmark"></i>';
            }
        });
    }

    if (themeBtn) {
        themeBtn.addEventListener('click', () => {
            state.theme = state.theme === 'dark' ? 'light' : 'dark';
            localStorage.setItem('dcsc_theme', state.theme);
            document.documentElement.setAttribute('data-theme', state.theme);
            themeBtn.innerHTML = state.theme === 'dark' ? '<i class="fa-solid fa-moon"></i>' : '<i class="fa-solid fa-sun"></i>';
        });
    }

    // Hamburger 3-Line Mobile Drawer
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('nav-menu');
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', () => navMenu.classList.toggle('active'));
    }
}

function initTheme() {
    document.documentElement.setAttribute('data-theme', state.theme);
}

// --- Post Lightbox Modal ---

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


// --- Sci-Lab Game 1: Chemical Reaction Beaker Simulator ---
function initSciLab() {
    const elemBtns = document.querySelectorAll('.elem-btn');
    const liquid = document.getElementById('beaker-liquid');
    const output = document.getElementById('reaction-output');
    const resetBtn = document.getElementById('reset-lab-btn');

    elemBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const elem = btn.getAttribute('data-elem');
            if (state.selectedElements.length < 2) {
                state.selectedElements.push(elem);
                btn.classList.add('selected');
                updateSciLabState();
            }
        });
    });

    if (resetBtn) {
        resetBtn.addEventListener('click', () => {
            state.selectedElements = [];
            elemBtns.forEach(b => b.classList.remove('selected'));
            liquid.className = 'liquid';
            output.innerHTML = '<span class="placeholder-text">Selected elements will appear here...</span>';
        });
    }
}

function updateSciLabState() {
    const liquid = document.getElementById('beaker-liquid');
    const output = document.getElementById('reaction-output');
    const elems = state.selectedElements;

    if (elems.length === 1) {
        output.innerHTML = `Added: <strong>${elems[0]}</strong>. Pick one more element!`;
        liquid.style.height = '45%';
    } else if (elems.length === 2) {
        liquid.style.height = '65%';
        const combo = elems.sort().join(' + ');

        if (combo === 'H2O + Na') {
            liquid.className = 'liquid explosion';
            output.innerHTML = `💥 <strong>EXPLOISVE REACTION!</strong><br>2Na + 2H₂O → 2NaOH + H₂ ↑ (Violent Exothermic Reaction)`;
            triggerConfetti();
        } else if (combo === 'HCl + NaOH') {
            liquid.className = 'liquid bubbling';
            output.innerHTML = `🧪 <strong>NEUTRALIZATION REACTION</strong><br>HCl + NaOH → NaCl + H₂O (Salt + Water Solution)`;
        } else if (combo === 'H2 + O2') {
            liquid.className = 'liquid bubbling';
            output.innerHTML = `⚡ <strong>COMBUSTION SYNTHESIS</strong><br>2H₂ + O₂ → 2H₂O (Water Molecules Formed)`;
        } else {
            liquid.className = 'liquid bubbling';
            output.innerHTML = `⚗️ Mixed <strong>${combo}</strong> inside beaker!`;
        }
    }
}

// --- Sci-Lab Game 2: 10-Question Science Quiz Engine (INLINE FEEDBACK, NO ALERT POPUPS!) ---
function loadQuizQuestion() {
    const quizQuestions = [
        { q: "What is the atomic symbol for Gold?", options: ["Au", "Ag", "Fe", "Go"], ans: 0 },
        { q: "Which element has atomic number 1?", options: ["Helium", "Hydrogen", "Oxygen", "Lithium"], ans: 1 },
        { q: "What gas is produced when Sodium (Na) reacts with Water (H₂O)?", options: ["Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen"], ans: 2 },
        { q: "Which element is essential for organic chemistry life forms?", options: ["Carbon", "Neon", "Argon", "Silicon"], ans: 0 },
        { q: "What is the speed of light in a vacuum approximately?", options: ["3 x 10^8 m/s", "1.5 x 10^8 m/s", "3 x 10^6 m/s", "3000 m/s"], ans: 0 },
        { q: "Which particle carries a negative electric charge?", options: ["Proton", "Neutron", "Electron", "Photon"], ans: 2 },
        { q: "What is the SI unit of Force?", options: ["Joule", "Newton", "Pascal", "Watt"], ans: 1 },
        { q: "Which planet in our solar system has the most prominent rings?", options: ["Jupiter", "Mars", "Saturn", "Neptune"], ans: 2 },
        { q: "What pH value represents a neutral solution?", options: ["0", "7", "14", "5"], ans: 1 },
        { q: "What force holds planets in orbit around the Sun?", options: ["Electrostatic", "Gravity", "Magnetic", "Nuclear Strong"], ans: 1 }
    ];

    const q = quizQuestions[state.currentQuizIndex];
    const qBox = document.getElementById('quiz-box');
    if (!qBox || !q) return;

    let optionsHTML = '';
    q.options.forEach((opt, idx) => {
        optionsHTML += `<button class="btn-secondary quiz-opt-btn" style="width:100%; text-align:left; justify-content:flex-start; margin-bottom:10px; font-size:1rem;" onclick="checkQuizAnswer(${idx})">${opt}</button>`;
    });

    qBox.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
            <span style="color:var(--cyan-glow); font-weight:700;">QUESTION ${state.currentQuizIndex + 1} OF 10</span>
            <span style="background:var(--blue-accent); padding:4px 12px; border-radius:12px; font-size:0.85rem; font-weight:700;">Score: ${state.quizScore} pts</span>
        </div>
        <h3 style="font-family:var(--font-heading); font-size:1.25rem; margin-bottom:20px; color:var(--text-primary); text-transform:none;">${q.q}</h3>
        ${optionsHTML}
        <div id="quiz-feedback" style="margin-top:16px; font-weight:700; font-size:0.95rem; min-height:24px;"></div>
    `;
}

function checkQuizAnswer(selectedIdx) {
    const quizQuestions = [
        { q: "What is the atomic symbol for Gold?", options: ["Au", "Ag", "Fe", "Go"], ans: 0 },
        { q: "Which element has atomic number 1?", options: ["Helium", "Hydrogen", "Oxygen", "Lithium"], ans: 1 },
        { q: "What gas is produced when Sodium (Na) reacts with Water (H₂O)?", options: ["Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen"], ans: 2 },
        { q: "Which element is essential for organic chemistry life forms?", options: ["Carbon", "Neon", "Argon", "Silicon"], ans: 0 },
        { q: "What is the speed of light in a vacuum approximately?", options: ["3 x 10^8 m/s", "1.5 x 10^8 m/s", "3 x 10^6 m/s", "3000 m/s"], ans: 0 },
        { q: "Which particle carries a negative electric charge?", options: ["Proton", "Neutron", "Electron", "Photon"], ans: 2 },
        { q: "What is the SI unit of Force?", options: ["Joule", "Newton", "Pascal", "Watt"], ans: 1 },
        { q: "Which planet in our solar system has the most prominent rings?", options: ["Jupiter", "Mars", "Saturn", "Neptune"], ans: 2 },
        { q: "What pH value represents a neutral solution?", options: ["0", "7", "14", "5"], ans: 1 },
        { q: "What force holds planets in orbit around the Sun?", options: ["Electrostatic", "Gravity", "Magnetic", "Nuclear Strong"], ans: 1 }
    ];

    const q = quizQuestions[state.currentQuizIndex];
    const fb = document.getElementById('quiz-feedback');
    const buttons = document.querySelectorAll('.quiz-opt-btn');

    buttons.forEach(btn => btn.disabled = true);

    if (selectedIdx === q.ans) {
        state.quizScore += 10;
        if (fb) fb.innerHTML = `<span style="color:var(--green-glow);"><i class="fa-solid fa-circle-check"></i> Correct Answer! (+10 Points)</span>`;
        triggerConfetti();
    } else {
        if (fb) fb.innerHTML = `<span style="color:#EF4444;"><i class="fa-solid fa-circle-xmark"></i> Incorrect! Correct answer was: ${q.options[q.ans]}</span>`;
    }

    setTimeout(() => {
        state.currentQuizIndex = (state.currentQuizIndex + 1) % quizQuestions.length;
        loadQuizQuestion();
    }, 1400);
}

// --- Sci-Lab Game 3: Physics Gravity & Orbital Sandbox ---
function initPhysicsOrbitSandbox() {
    const canvas = document.getElementById('orbit-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    let width = canvas.width = canvas.parentElement.clientWidth || 600;
    let height = canvas.height = 420;

    const sun = { x: width / 2, y: height / 2, mass: 1200, radius: 24 };
    const planets = [
        { x: width / 2, y: height / 2 - 100, vx: 3.2, vy: 0, radius: 7, color: '#00F2FE' },
        { x: width / 2 + 150, y: height / 2, vx: 0, vy: 2.5, radius: 9, color: '#FFD700' }
    ];

    canvas.addEventListener('click', (e) => {
        const rect = canvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;
        planets.push({
            x: mouseX, y: mouseY,
            vx: (Math.random() - 0.5) * 4,
            vy: (Math.random() - 0.5) * 4,
            radius: Math.random() * 5 + 4,
            color: ['#00F2FE', '#FFD700', '#10B981', '#7C3AED'][Math.floor(Math.random() * 4)]
        });
    });

    function animateOrbit() {
        ctx.fillStyle = 'rgba(8, 12, 20, 0.2)';
        ctx.fillRect(0, 0, width, height);

        ctx.beginPath();
        ctx.arc(sun.x, sun.y, sun.radius, 0, Math.PI * 2);
        ctx.fillStyle = '#FFD700';
        ctx.shadowBlur = 25;
        ctx.shadowColor = '#FFD700';
        ctx.fill();
        ctx.shadowBlur = 0;

        planets.forEach(p => {
            let dx = sun.x - p.x;
            let dy = sun.y - p.y;
            let dist = Math.hypot(dx, dy);

            if (dist > sun.radius) {
                let force = (sun.mass) / (dist * dist);
                p.vx += (dx / dist) * force;
                p.vy += (dy / dist) * force;
            }

            p.x += p.vx;
            p.y += p.vy;

            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fillStyle = p.color;
            ctx.fill();
        });

        requestAnimationFrame(animateOrbit);
    }
    animateOrbit();
}

// --- Live Member ID Card Generator ---
function initJoinForm() { updateLiveIDCard(); }

function updateLiveIDCard() {
    const name = document.getElementById('in-name')?.value || 'MEMBER NAME';
    const roll = document.getElementById('in-roll')?.value || '----';
    const batch = document.getElementById('in-batch')?.value || '----';
    const interest = document.getElementById('in-interest')?.value || 'Physics & Astronomy';

    if (document.getElementById('id-disp-name')) document.getElementById('id-disp-name').innerText = name.toUpperCase();
    if (document.getElementById('id-disp-roll')) document.getElementById('id-disp-roll').innerText = roll;
    if (document.getElementById('id-disp-batch')) document.getElementById('id-disp-batch').innerText = batch;
    if (document.getElementById('id-disp-interest')) document.getElementById('id-disp-interest').innerText = interest;
}

function handleJoinSubmit(e) {
    e.preventDefault();
    triggerConfetti();
}

// --- Certificate Generator ---
function initCertForm() {}

function generateCertificate(e) {
    e.preventDefault();
    const name = document.getElementById('cert-name').value;
    const eventName = document.getElementById('cert-event').value;

    document.getElementById('out-cert-name').innerText = name;
    document.getElementById('out-cert-event').innerText = eventName;

    triggerConfetti();
}

function triggerConfetti() {
    if (typeof confetti === 'function') {
        confetti({ particleCount: 80, spread: 70, origin: { y: 0.6 } });
    }
}

// --- LANGUAGE TOGGLE & TRANSLATION SYSTEM ---
document.addEventListener('DOMContentLoaded', () => {
    const langBtn = document.getElementById('lang-btn');
    const langIndicator = document.getElementById('lang-indicator');
    
    if (langBtn) {
        let currentLang = localStorage.getItem('dcsc-lang') || 'en';
        
        const setLanguage = (lang) => {
            document.documentElement.setAttribute('data-lang', lang);
            if (langIndicator) {
                langIndicator.textContent = lang.toUpperCase();
            }
            document.querySelectorAll('[data-en][data-bn]').forEach(el => {
                const text = el.getAttribute(`data-${lang}`);
                if (text) {
                    el.textContent = text;
                }
            });
            localStorage.setItem('dcsc-lang', lang);
        };

        // Initialize language
        setLanguage(currentLang);

        langBtn.addEventListener('click', () => {
            currentLang = currentLang === 'en' ? 'bn' : 'en';
            setLanguage(currentLang);
        });
    }
});
