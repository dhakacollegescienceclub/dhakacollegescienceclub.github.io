import re

# Read the concatenated file (using index.html since all files have the same concatenated content)
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all individual HTML documents
docs = re.findall(r'(<!DOCTYPE html>.*?</html>)', content, flags=re.DOTALL)

title_to_file = {
    "About Us | Dhaka College Science Club": "about.html",
    "Achievements | Dhaka College Science Club": "achievements.html",
    "Certificate Verification Portal | Dhaka College Science Club": "cert-verify.html",
    "Committee | Dhaka College Science Club": "committee.html",
    "Intra Science Festival & Freshers’ Orientation 2025 | DCSC": "event-freshers.html",
    "Intra Science Festival & Freshers Orientation 2025 | DCSC": "event-freshers.html",
    "DCSC AI NeuroVerse 2026 | DCSC": "event-neuroverse.html",
    "Everything About Quizzing | DCSC": "event-quizzing.html",
    "Studying in the U.S. | DCSC": "event-us.html",
    "Events & Festivals | Dhaka College Science Club": "events.html",
    "Photo Gallery | Dhaka College Science Club": "gallery.html",
    "Dhaka College Science Club (DCSC) | Official Portal": "index.html",
    "Join DCSC & Certificates | Dhaka College Science Club": "join.html",
    "Posts & News | Dhaka College Science Club": "posts.html",
    "Atomic Orbital & Bohr Model Simulator | DCSC Sci-Lab": "scilab-chemistry.html",
    "Chemical Beaker Reaction Simulator | DCSC Sci-Lab": "scilab-reaction.html",
    "Physics Gravity & Planet Sandbox | DCSC Sci-Lab": "scilab-sandbox.html",
    "10-Question National Science Quiz | DCSC Sci-Lab": "scilab-quiz.html",
    "Interactive Sci-Lab Hub | Dhaka College Science Club": "scilab.html",
    "Wall Magazine - Wednesday Wonders | Dhaka College Science Club": "wall-magazine.html",
}

recovered_files = 0

for doc in docs:
    # Find the title
    match = re.search(r'<title>(.*?)</title>', doc)
    if match:
        title = match.group(1).strip()
        filename = title_to_file.get(title)
        
        if not filename and "Orientation 2025" in title:
            filename = "event-freshers.html"
            
        if filename:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(doc)
            recovered_files += 1
            print(f"Recovered {filename}")
        else:
            print(f"Unknown title: {title}")
    else:
        print("No title found in document")

print(f"Successfully recovered {recovered_files} files.")
