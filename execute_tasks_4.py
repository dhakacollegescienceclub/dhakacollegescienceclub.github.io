import re

# Base template reading
with open('events.html', 'r', encoding='utf-8') as f:
    base = f.read()

# Remove the events section from the base template
base = re.sub(r'<section class="section-padding">.*?</section>', '<!-- EVENT_CONTENT -->', base, flags=re.DOTALL)
base = re.sub(r'<h2>Events</h2>', '<h2>Event Details</h2>', base)

# Helper to generate pages
def create_event_page(filename, img_src, title, date_venue, body):
    content = f'''
        <section class="section-padding" style="max-width: 800px; margin: 0 auto;">
            <div style="border-radius: 20px; overflow: hidden; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1);">
                <img src="{img_src}" style="width: 100%; height: auto; display: block;" alt="{title}">
            </div>
            <h1 style="font-family: var(--font-heading); font-size: 2.5rem; margin-bottom: 15px; color: #fff;">{title}</h1>
            <div style="color: var(--cyan-glow); font-weight: 600; margin-bottom: 25px; font-size: 1.1rem;">
                {date_venue}
            </div>
            <div style="color: var(--text-secondary); font-size: 1.1rem; line-height: 1.8; white-space: pre-line;">
                {body}
            </div>
            <div style="margin-top: 40px;">
                <a href="events.html" class="btn-outline"><i class="fa-solid fa-arrow-left"></i> Back to Events</a>
            </div>
        </section>
'''
    page = base.replace('<!-- EVENT_CONTENT -->', content)
    # Fix the title
    page = re.sub(r'<title>.*?</title>', f'<title>{title} | DCSC</title>', page)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(page)

# --- E1: NeuroVerse ---
e1_body = '''The DCSC AI NeuroVerse 2026 is an upcoming tech and AI fest hosted by Dhaka College Science Club. 
More details will be updated soon. Stay tuned!'''
create_event_page('event-neuroverse.html', 'image/e1.jpg', 'DCSC AI NeuroVerse 2026', '12 October 2026 | Dhaka College', e1_body)

# --- E4: Quizzing ---
e4_body = '''Dhaka College Science Club is presenting a special session on “Everything About Quizzing”.

The session will be conducted by Quizmaster Azmain Tahmid bhaiya, Former Head of Quiz and Former Quizzer of DC ULKA, who will guide participants through quiz basics, preparation methods and resources.

Date: 11th December, 2025
Time: 10:30 AM
Venue: Shaheed A. N. M. Najib Uddan Khan Khurram Auditorium, Dhaka College, Dhaka.'''
create_event_page('event-quizzing.html', 'image/e4.jpg', 'Everything About Quizzing', '11 December 2025 | Khurram Auditorium', e4_body)

# --- E5: US Study ---
e5_body = '''Dhaka College Science Club, along with EdBridge Scholars, is presenting a special session on “Everything You Need to Know About Studying in the U.S.”

The session will be led by Abrar Azim Hrittek (University of British Columbia), who will share key insights on admissions, scholarships and studying abroad.

Date : 15 November,2025 
Time : 10:00 PM
Join us and take the first step toward your U.S. academic journey.'''
create_event_page('event-us.html', 'image/e5.jpg', 'Studying in the U.S.', '15 November 2025 | Online / DCSC', e5_body)

# --- E6: Freshers ---
e6_body = '''“Somewhere, something incredible is waiting to be known.”
— Carl Sagan

Dhaka College Science Club (DCSC) proudly presents one of the most anticipated events of the year — DCSC Intra Science Festival and Freshers’ Orientation 2025!

This Intra Science Festival is your chance to challenge yourself, explore your interests in science, and connect with fellow students. Whether you're curious about the mysteries of nature and the wonders of discovery—there's something here for every science enthusiast.
Don't miss this opportunity! Your classmates will be there competing, learning, and making memories. We're eagerly waiting for your presence. Come join us and make this Intra Fest unforgettable.

Eligibility:
Only the intermediate-level students of Dhaka College are allowed to participate in this Intra Science Festival.
To make it easier for everyone to participate, we're holding both offline and online events.
Here is the full list of events we'll be arranging in the DCSC Intra Science Festival and Freshers' Orientation 2025:

OFFLINE EVENTS:
(Written Competitions):
1. Science Olympiad
2. Solo Quiz
3. Calculus Combat
4. IQ Test with Criminal Case Solving
5. Sudoku Race

(Display Competitions):
1. Wall Magazine
2. Project Display (Mechanical / Non-Mechanical / IT)
3. Scrapbook

(Gaming):
1. FC 26 Tournament

ONLINE EVENTS:
1. Designers' Hunt
2. Photography Submission
3. Sci-fi Story Writing

Freshers’ Orientation:
Just recently, Dhaka College Science Club successfully completed the recruitment of our 27th batch members, and we're amazed by the incredible response from so many talented and passionate students. DCSC has always been home to brilliant minds, creative thinkers, and future innovators, and we can hardly wait to welcome this new group of freshers into our family.

Through this orientation program, we will officially welcome you with a celebration you won't forget. Every new member of the 27th batch is expected to be present, as this is your moment to become part of something special.

#Tunneling_beyond_Barriers

For any query,
Sadman Sadaf
President
Executive Committee 2024-25
Contact: +8801743-389009
https://www.facebook.com/sadman.sadaff

Shahriar Samir
General Secretary
Executive Committee 2024-25
Contact: +8801920-248292
https://www.facebook.com/shahriarsamir.me'''
create_event_page('event-freshers.html', 'image/e6.jpg', 'Intra Science Festival & Freshers’ Orientation 2025', 'Upcoming | Dhaka College', e6_body)

print("Tasks 5 (dedicated pages) completed.")
