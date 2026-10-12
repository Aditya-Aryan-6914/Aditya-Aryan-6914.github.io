"""
Single source of truth for the portfolio. Edit this file and rebuild.
Only facts you have told me are filled in. Anything set to None is hidden on the site
until you fill it in (email, LinkedIn, phone, resume PDF...).
"""

def P(frm, via, to, accent):
    return {"from": frm, "via": via, "to": to, "accent": accent}

CRIMSON = P("#24060b", "#6e0d1d", "#09070a", "#ff3d5a")
AMBER = P("#1c1003", "#6b3c06", "#0a0806", "#ffb547")
OCEAN = P("#04121f", "#0f4c6e", "#05080d", "#4cc9ff")
VIOLET = P("#120822", "#3d1a6e", "#07060c", "#b98bff")
JADE = P("#03150f", "#0d5a40", "#050a08", "#46e3a8")

PROFILE = {
    "full_name": "Aditya Aryan",
    "first_name": "ADITYA",
    "series_tag": "THE SERIES",
    "original_label": "AN ARYAN ORIGINAL",
    "role": "Full Stack Developer",
    "tagline": ["Full Stack Developer", "AI / ML Engineer", "Cloud Engineer"],
    "intro": (
        "A B.Tech Computer Science (AI & ML) student, IIT Madras Data Science scholar and "
        "full stack developer who builds web platforms with Django and Flask, contributes to "
        "open source, and is heading into cloud-native engineering."
    ),
    "location": "Kolhapur, Maharashtra",
    "email": None,                      # e.g. "you@example.com"  (hidden while None)
    "phone": None,
    "links": {
        "github": "https://github.com/Aditya-Aryan-6914",
        "linkedin": None,               # e.g. "https://www.linkedin.com/in/your-handle/"
        "website": "https://adityaaryan.me",
    },
    "resume_pdf": "files/Aditya_Aryan_Resume.pdf",   # put the PDF in static/files/ to enable the button
    "interests": ["Open Source", "Cloud-Native & DevOps", "Cybersecurity", "AI / ML"],
    "about": [
        "I am a second-year B.Tech student in Computer Science (AI & ML) at KIT's College of Engineering, "
        "Kolhapur, and I am also pursuing the B.Sc in Data Science and Programming from IIT Madras.",
        "I enjoy turning ideas into working products: a Django e-commerce platform, a Flask based campus "
        "attendance tracker, and the website that served 5k+ users during my college's cultural fest.",
        "Outside coursework I contribute to open source (compliance-trestle, CNCF / Cartografos), solve "
        "problems on CodeChef and LeetCode, and run a small coding community on campus.",
    ],
}

EDUCATION = [
    {"school": "KIT's College of Engineering", "place": "Kolhapur",
     "degree": "B.Tech Computer Science (AI & ML)", "period": "September 2025 – Present", "score": "CGPA 9.0"},
    {"school": "IIT Madras", "place": "Online",
     "degree": "B.Sc in Data Science and Programming", "period": "May 2025 – Present", "score": "CGPA 8.25"},
    {"school": "Sainik School Kunjpura", "place": "Haryana",
     "degree": "CBSE Class 10 and Class 12", "period": "School years", "score": "91% in Class 10 · 70.6% in Class 12"},
]

LEADERSHIP = [
    {"role": "Google Gemini Campus Ambassador", "org": "Google", "period": "", "points": []},
    {"role": "Technical Team Member", "org": "KIT Cultural Committee", "period": "Since November 2025",
     "points": ["Designed and maintain the Cultural Committee website.",
                "Manage registration and feedback forms for campus events."]},
    {"role": "Sponsorship Department", "org": "Pradox, IIT Madras", "period": "November 2025 – June 2026",
     "points": ["Handled sponsor outreach and event coordination."]},
]

# ---------------------------------------------------------------------------
# Projects ("Originals").  Omit "github" when there is no public repo.
# ---------------------------------------------------------------------------
PROJECTS = [
    {
        "id": "campustrack", "title": "CampusTrack", "year": "2026", "genre": "Flask • Web • Campus",
        "logline": "A Flask based campus attendance and in/out register, built as a four person mini project.",
        "stack": ["Python", "Flask", "HTML", "CSS", "JavaScript"],
        "build": ["Built the in/out register web app (repo: InOut-register) with a team of four at KIT's College of Engineering, Kolhapur.",
                  "Deployed live at campustrack.adityaaryan.me."],
        "features": ["Campus in/out and attendance tracking", "Team project with four contributors", "Live deployment on a custom subdomain"],
        "metrics": [{"value": "4", "label": "member team"}, {"value": "Live", "label": "campustrack.adityaaryan.me"}],
        "github": "https://github.com/Aditya-Aryan-6914/InOut-register",
        "live": "https://campustrack.adityaaryan.me",
        "palette": CRIMSON, "motif": "flow",
    },
    {
        "id": "meraki", "title": "Meraki", "year": "2026", "genre": "Web • UI • Authentication",
        "logline": "The Cultural Committee website that handled 5k+ users during the Meraki 2026 event.",
        "stack": ["HTML", "CSS", "JavaScript", "Authentication"],
        "build": ["Worked on the UI and authentication for the Cultural Committee's Meraki website.",
                  "The site handled 5k+ users during Meraki 2026."],
        "features": ["UI design and implementation", "User authentication", "Registration and feedback forms"],
        "metrics": [{"value": "5k+", "label": "users during Meraki 2026"}],
        "palette": AMBER, "motif": "tenants",
    },
    {
        "id": "django-ecommerce", "title": "Django E-commerce Web App", "year": "2026", "genre": "Django • Full Stack • Retail",
        "logline": "An e-commerce web application built with Django using the MVC pattern.",
        "stack": ["Python", "Django", "SQLite", "MySQL"],
        "build": ["Built an e-commerce web application with Django following MVC architecture.",
                  "Implemented user authentication, URL routing and database integration with SQLite/MySQL."],
        "features": ["MVC architecture", "User authentication", "URL routing", "SQLite / MySQL storage"],
        "metrics": [],
        "palette": OCEAN, "motif": "shield",
    },
    {
        "id": "compliance-trestle", "title": "compliance-trestle", "year": "Open Source", "genre": "Open Source • Compliance • Security",
        "logline": "Open-source contribution to a compliance-as-code platform built on NIST's OSCAL standard.",
        "stack": ["Python", "OSCAL", "Git", "GitHub"],
        "build": ["Contributed to compliance-trestle, an open-source compliance-as-code tooling platform using NIST's OSCAL standard.",
                  "Solved a digital signature problem in the project."],
        "features": ["Compliance-as-code tooling", "NIST OSCAL standard", "Digital signature fix"],
        "metrics": [],
        "palette": VIOLET, "motif": "shield",
    },
    {
        "id": "mergemail", "title": "MergeMail", "year": "2026", "genre": "Utility • Email",
        "logline": "A single place to check multiple mail accounts.",
        "stack": ["Web"],
        "build": ["Built MergeMail so several mail accounts can be checked from one place."],
        "features": ["Multiple mail accounts in one view"],
        "metrics": [],
        "github": "https://github.com/Aditya-Aryan-6914/MergeMail",
        "palette": JADE, "motif": "flow",
    },
    {
        "id": "nullpointer", "title": "NullPointer", "year": "Hackathon", "genre": "Hackathon • Team Project",
        "logline": "Team project built for the AGTechathon 2.0 hackathon.",
        "stack": ["Teamwork", "Prototyping"],
        "build": ["Built with the NullPointer team at AGTechathon 2.0."],
        "features": ["Hackathon prototype", "Team collaboration"],
        "metrics": [],
        "github": "https://github.com/Aditya-Aryan-6914/NullPointer",
        "palette": AMBER, "motif": "tenants",
    },
]

ACHIEVEMENTS = [
    {"title": "School Captain", "org": "Sainik School Kunjpura", "detail": "Led the student body as School Captain.", "palette": CRIMSON},
    {"title": "District-Level Debate Champion", "org": "Debate", "detail": "Won the district-level debate competition.", "palette": AMBER},
    {"title": "500 CodeChef Problems", "org": "CodeChef", "detail": "Solved 500 difficult-level questions.", "palette": JADE},
    {"title": "Google Gemini Campus Ambassador", "org": "Google", "detail": "Represents Google Gemini on campus.", "palette": OCEAN},
    {"title": "Top 1% in CBSE Class 10", "org": "CBSE", "detail": "Scored 91% in Class 10 (top 1%).", "palette": VIOLET},
    {"title": "AISSEE Qualified", "org": "NTA", "detail": "Cleared the All India Sainik School Entrance Examination.", "palette": CRIMSON},
]

CERTIFICATIONS = [
    {"issuer": "Google Cloud", "name": "Google Cloud Deployment, Management and Skill Boost", "link": None},
    {"issuer": "Google Cloud", "name": "Introduction to Security Principles in Cloud Computing", "link": None},
]

SKILL_CATEGORIES = [
    {"id": "lang", "title": "Languages", "subtitle": "How I think in code", "skills": [
        {"name": "Python", "mono": "Py"}, {"name": "C", "mono": "C"}, {"name": "Rust", "mono": "Rs"},
        {"name": "JavaScript", "mono": "JS"}]},
    {"id": "web", "title": "Web & Frameworks", "subtitle": "Interfaces and servers", "skills": [
        {"name": "Django", "mono": "Dj"}, {"name": "Flask", "mono": "Fl"}, {"name": "Tailwind", "mono": "Tw"},
        {"name": "Bootstrap", "mono": "Bs"}, {"name": "WordPress", "mono": "Wp"}]},
    {"id": "data", "title": "Databases", "subtitle": "Where data lives", "skills": [
        {"name": "MongoDB", "mono": "Mg"}, {"name": "SQL", "mono": "SQL"}, {"name": "SQLite / MySQL", "mono": "My"}]},
    {"id": "cloud", "title": "Cloud & DevOps", "subtitle": "Shipping and running it", "skills": [
        {"name": "Google Cloud", "mono": "GCP"}, {"name": "Docker", "mono": "Dk", "note": "Basics"},
        {"name": "Kubernetes", "mono": "K8", "note": "Fundamentals"}, {"name": "Linux (CLI)", "mono": "Lx"}]},
    {"id": "tools", "title": "Tools", "subtitle": "Daily drivers", "skills": [
        {"name": "Git", "mono": "Git"}, {"name": "GitHub", "mono": "GH"}, {"name": "VS Code", "mono": "VS"},
        {"name": "Google Workspace", "mono": "GW"}]},
    {"id": "human", "title": "Languages Spoken", "subtitle": "Beyond code", "skills": [
        {"name": "English", "mono": "En", "note": "Professional"}, {"name": "Hindi", "mono": "Hi", "note": "Professional"},
        {"name": "Japanese", "mono": "Ja", "note": "N5, learning"}]},
]

SKILL_EVIDENCE = {
    "Django": ["Django E-commerce Web App"],
    "Flask": ["CampusTrack"],
    "Git": ["compliance-trestle", "CNCF / Cartografos"],
    "GitHub": ["Fork, branch and pull request workflow", "Open-source contributions"],
    "Google Cloud": ["Google Cloud Deployment, Management and Skill Boost", "Security Principles in Cloud Computing"],
    "JavaScript": ["Meraki"],
    "Python": ["compliance-trestle", "CampusTrack", "Django E-commerce Web App"],
}

# ---------------------------------------------------------------------------
# Journey: seasons and episodes. Palettes are decoration only.
# ---------------------------------------------------------------------------
def ep(code, title, desc, tags, runtime, palette):
    return {"code": code, "title": title, "description": desc, "tags": tags, "runtime": runtime, "palette": palette}

SEASONS = [
    {"number": 1, "title": "The Foundation", "period": "School years",
     "synopsis": "Discipline, leadership and a love of debate at Sainik School Kunjpura.",
     "episodes": [
        ep("S01 E01", "The Entrance", "Cleared the All India Sainik School Entrance Examination.", ["AISSEE"], "Entrance exam", AMBER),
        ep("S01 E02", "The Captain", "Served as School Captain, won the district-level debate title and represented the school in volleyball.", ["Leadership", "Debate", "Volleyball"], "Sainik School Kunjpura", CRIMSON),
        ep("S01 E03", "The Scorecard", "91% in CBSE Class 10 (top 1%) and 70.6% in Class 12 (top 5%).", ["CBSE", "Top 1%"], "Boards", OCEAN),
     ]},
    {"number": 2, "title": "Two Degrees", "period": "2025 – Present",
     "synopsis": "A B.Tech in the classroom and a Data Science degree from IIT Madras online.",
     "episodes": [
        ep("S02 E01", "Data Science", "Started the IIT Madras B.Sc in Data Science and Programming, now at CGPA 8.25.", ["IIT Madras", "CGPA 8.25"], "May 2025 – Present", VIOLET),
        ep("S02 E02", "The Engineer", "Began B.Tech Computer Science (AI & ML) at KIT's College of Engineering, Kolhapur, now at CGPA 9.0.", ["B.Tech", "AI & ML", "CGPA 9.0"], "Sept 2025 – Present", JADE),
     ]},
    {"number": 3, "title": "Learning to Build", "period": "2025 – 2026",
     "synopsis": "Shipping real software: campus tools, e-commerce and a fest website.",
     "episodes": [
        ep("S03 E01", "The Builder", "Built a Django e-commerce web app with authentication, routing and SQLite/MySQL.", ["Django", "MVC"], "Django", OCEAN),
        ep("S03 E02", "The Fest", "Designed the UI and authentication for Meraki, which served 5k+ users in 2026.", ["Meraki", "5k+ users"], "Meraki 2026", AMBER),
        ep("S03 E03", "The Tracker", "Led a four person team to build and deploy CampusTrack.", ["Flask", "Team of 4"], "2026", CRIMSON),
     ]},
    {"number": 4, "title": "Open Source & Community", "period": "Ongoing",
     "synopsis": "Contributing back, and building a community around code.",
     "episodes": [
        ep("S04 E01", "The Contributor", "Contributed to compliance-trestle (NIST OSCAL) and fixed a digital signature problem.", ["Open Source", "OSCAL"], "compliance-trestle", VIOLET),
        ep("S04 E02", "The Documenter", "Fixing documentation issues for CNCF / Cartografos with fork, branch and PR workflows.", ["CNCF", "Docs"], "Cartografos", JADE),
        ep("S04 E03", "The Organiser", "Google Gemini Campus Ambassador, Cultural Committee tech team and Pradox sponsorship team.", ["Gemini", "Pradox", "Cultural Committee"], "Nov 2025 – Present", AMBER),
     ]},
    {"number": 5, "title": "What's Next", "period": "Now streaming",
     "synopsis": "Cloud-native engineering, security and a few more languages.",
     "episodes": [
        ep("S05 E01", "The Next Chapter", "Exploring Kubernetes, Docker, DevOps, observability and cybersecurity, plus Rust and Japanese on the side.", ["Cloud-Native", "DevOps", "Security", "Rust", "Japanese"], "In production", OCEAN),
     ]},
]

TOP_PICKS = [
    {"label": "Biggest audience", "title": "Meraki 2026", "detail": "5k+ users on a site I worked on", "palette": CRIMSON},
    {"label": "Academic high", "title": "CGPA 9.0", "detail": "B.Tech CSE (AI & ML), KIT", "palette": JADE},
    {"label": "Second degree", "title": "IIT Madras", "detail": "B.Sc Data Science, CGPA 8.25", "palette": VIOLET},
    {"label": "Problem solving", "title": "500", "detail": "Difficult CodeChef questions", "palette": AMBER},
    {"label": "Open source", "title": "compliance-trestle", "detail": "Fixed a digital signature problem", "palette": OCEAN},
    {"label": "Campus ambassador", "title": "Google Gemini", "detail": "Representing Google on campus", "palette": CRIMSON},
    {"label": "Leadership", "title": "School Captain", "detail": "Sainik School Kunjpura", "palette": AMBER},
    {"label": "Public speaking", "title": "Debate Champion", "detail": "District level", "palette": JADE},
    {"label": "Boards", "title": "Top 1%", "detail": "91% in CBSE Class 10", "palette": VIOLET},
    {"label": "Cloud credential", "title": "Google Cloud", "detail": "Two certifications", "palette": OCEAN},
]

INTRO_SLIDES = [
    {"kicker": "Education", "title": "B.Tech · AI & ML", "lines": ["KIT's College of Engineering, Kolhapur", "September 2025 – Present"], "chips": ["CGPA 9.0"]},
    {"kicker": "Second degree", "title": "IIT Madras", "lines": ["B.Sc in Data Science and Programming", "May 2025 – Present"], "chips": ["CGPA 8.25"]},
    {"kicker": "Skills", "title": "Python first.", "lines": ["Django, Flask, JavaScript, Tailwind, Bootstrap", "MongoDB, SQL · Git, Docker, Google Cloud"], "chips": ["Python", "Django", "Flask", "JavaScript", "Google Cloud"]},
    {"kicker": "Projects", "title": "Originals", "lines": ["CampusTrack · Meraki · Django E-commerce", "compliance-trestle · MergeMail · NullPointer"]},
    {"kicker": "Leadership", "title": "Top Moments", "lines": ["Google Gemini Campus Ambassador", "School Captain · District Debate Champion", "500 CodeChef problems"]},
    {"kicker": "Current mission", "title": "Now exploring", "lines": ["Cloud-native · DevOps · Observability · Security"]},
]

VIEWER_PROFILES = [
    {"id": "aditya", "name": "Aditya", "blurb": "The full series, in order", "color": "#e5132b", "glyph": "A",
     "order": ["about", "journey", "originals", "picks", "skills", "moments", "blog", "story"]},
    {"id": "recruiter", "name": "Recruiter", "blurb": "Resume, achievements & skills first", "color": "#4cc9ff", "glyph": "R",
     "order": ["story", "moments", "skills", "originals", "about", "blog", "journey", "picks"]},
    {"id": "developer", "name": "Developer", "blurb": "Projects, stack & GitHub first", "color": "#46e3a8", "glyph": "</>",
     "order": ["originals", "skills", "blog", "journey", "moments", "about", "picks", "story"]},
    {"id": "reader", "name": "Reader", "blurb": "Blog posts & the story arc first", "color": "#ffb547", "glyph": "✦",
     "order": ["blog", "journey", "picks", "originals", "moments", "about", "skills", "story"]},
]
