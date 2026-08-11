import re

posts = [
    {
        "id": 1,
        "tag": "Memorial",
        "title": "July Mass Uprising Memorial",
        "desc": "July is not just a month — it is a symbol of courage, sacrifice, and change.",
        "img": "image/p1.jpg"
    },
    {
        "id": 2,
        "tag": "Prize Giving",
        "title": "Olympiad Hunt 4.0 Prize Giving Ceremony",
        "desc": "Dhaka College Science Club is pleased to reveal the vibrant Prize Giving Ceremony of Olympiad Hunt 4.0!",
        "img": "image/p2.1.jpg"
    },
    {
        "id": 3,
        "tag": "Olympiad",
        "title": "Olympiad Hunt - Talent Hunt 2026",
        "desc": "Olympiad Hunt: A day full of learning, excitement, and healthy competition.",
        "img": "image/p3.1.jpg"
    },
    {
        "id": 4,
        "tag": "Talent Hunt",
        "title": "DCSC Talent Hunt Inauguration",
        "desc": "The long awaited moment has finally arrived, the DCSC Talent Hunt has been officially inaugurated!",
        "img": "image/p4.1.jpg"
    },
    {
        "id": 5,
        "tag": "Greetings",
        "title": "Eid-ul-Adha Mubarak",
        "desc": "Eid-ul-Adha reminds us that true Qurbani is not measured by flesh or blood.",
        "img": "image/p5.jpg"
    },
    {
        "id": 6,
        "tag": "Statement",
        "title": "Condemnation of Cruelty",
        "desc": "Even as we claim to be superior as a nation, the harsh truth is proven by these images of cruelty.",
        "img": "image/p6.jpg"
    },
    {
        "id": 7,
        "tag": "Announcement",
        "title": "New Sub-Executive Committee Welcome",
        "desc": "It is a great moment for DCSC as we reveal our newly chosen Sub-Executive Committee members.",
        "img": "image/p7.jpg"
    },
    {
        "id": 8,
        "tag": "Ramadan Specials",
        "title": "Wednesday Wonders: Ramadan Specials 2026",
        "desc": "Wednesday Wonders Ramadan Specials 2026 successfully combined science with religion in perfect harmony.",
        "img": "image/p8.jpg"
    },
    {
        "id": 9,
        "tag": "Iftar Mahfil",
        "title": "Grand Iftar Mahfil",
        "desc": "The DCSC family came together for a warm and memorable Iftar Mahfil on March 7, 2026.",
        "img": "image/p9.1.jpg"
    },
    {
        "id": 10,
        "tag": "Greetings",
        "title": "Happy New Year 2026",
        "desc": "2025, the previous year was of mixed emotions, bringing both happiness and lessons.",
        "img": "image/p10.jpg"
    }
]

def generate_html(posts_list):
    html = ""
    for p in posts_list:
        html += f'''                    <div class="post-card animate-on-scroll">
                        <div class="post-media">
                            <img src="{p['img']}" alt="{p['title']}" class="post-img">
                        </div>
                        <div class="post-body">
                            <div style="font-size:0.8rem; color:var(--cyan-glow); font-weight:700; margin-bottom:6px;">{p['tag']}</div>
                            <h3 class="post-title">{p['title']}</h3>
                            <p style="color:var(--text-secondary); font-size:0.9rem; margin-bottom:16px;">{p['desc']}</p>
                            <button class="btn-primary" onclick="openPostModal({p['id']})">Read Full Story</button>
                        </div>
                    </div>\n'''
    return html

# 1. Update achievements.html (all 10)
with open('achievements.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
new_achievements_html = generate_html(posts)

# Regex to replace everything inside <div class="posts-grid">
content = re.sub(r'(<div class="posts-grid">).*?(</div>\s*</div>\s*</section>)', r'\1\n' + new_achievements_html + r'\2', content, flags=re.DOTALL)

with open('achievements.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Update index.html (only top 3)
with open('index.html', 'r', encoding='utf-8') as f:
    content2 = f.read()

new_index_html = generate_html(posts[:3])

content2 = re.sub(r'(<div class="posts-grid">).*?(</div>\s*<div style="text-align:center; margin-top:30px;">)', r'\1\n' + new_index_html + r'\2', content2, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content2)

print("Updated achievements.html and index.html")
