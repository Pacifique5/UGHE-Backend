"""Starting content taken from the UGHE homepage screenshot and ughe.org menus.

The Next.js app does not contain these strings. They live in PostgreSQL and
can be replaced from Django admin. Image and video addresses point at files
UGHE already publishes on its own site.
"""

PREDEFINED_USERNAME = "ughe_admin"
PREDEFINED_PASSWORD = "UGHE-admin-2026"
PREDEFINED_EMAIL = "admin@ughe.test"

LOGO_URL = "https://ughe.org/wp-content/uploads/2026/04/UGHE-H.png"

SITE = {
    "university_line": "UNIVERSITY OF",
    "name_line": "Global Health",
    "equity_line": "EQUITY",
    "logo_alt": "University of Global Health Equity",
    "logo_url": LOGO_URL,
    "search_placeholder": "Search UGHE",
    "show_search": True,
    "action_background_color": "#E6D4D8",
    "action_text_color": "#2C2426",
}

ACTION_LINKS = [
    {"label": "Apply", "url": "https://ughe.org/admission/"},
    {"label": "Get Involved", "url": "https://ughe.org/get-involved/"},
    {"label": "Meet the Team", "url": "https://ughe.org/leadership/"},
    {"label": "More", "url": "https://ughe.org/more/"},
]

NAVIGATION = [
    {
        "label": "About Us",
        "url": "",
        "children": [
            {"label": "Our Story", "url": "https://ughe.org/about"},
            {"label": "Leadership", "url": "https://ughe.org/leadership/"},
            {"label": "University Medalists", "url": "https://ughe.org/university-medalists/"},
        ],
    },
    {
        "label": "Academics",
        "url": "",
        "children": [
            {"label": "School of Medicine", "url": "https://ughe.org/school-of-medicine/"},
            {
                "label": "Bachelor of Medicine, Bachelor of Surgery (MBBS)",
                "url": "https://ughe.org/bachelor-of-medicine-bachelor-of-surgery-mbbs/",
            },
            {
                "label": "Academic Departments",
                "url": "https://ughe.org/academics/#AcademicDepartments",
            },
            {
                "label": "Kolokotrones Deanship of School of Medicine",
                "url": "https://ughe.org/kolokotrones-deanship/",
            },
            {"label": "Graduate Programs", "url": "https://ughe.org/academics/"},
            {
                "label": "Master of Science in Global Health Delivery (MGHD)",
                "url": "https://ughe.org/master-of-science-in-global-health-delivery-mghd/",
            },
            {
                "label": "Masters in Global Nursing Leadership (MGLN)",
                "url": "https://ughe.org/masters-in-global-nursing-leadership-mgnl/",
            },
            {
                "label": "Health Professions Education Program (HPE)",
                "url": "https://ughe.org/health-professions-education-hpe-2/",
            },
            {
                "label": "General Surgery Residency Program (MMed/FCS-ECSA)",
                "url": "https://go.ughe.org/residency",
            },
            {
                "label": "Professional and Executive Programs",
                "url": "https://ughe.org/professional-and-executive-education-programs/",
            },
            {
                "label": "Executive Education Programs",
                "url": "https://ughe.org/centre-for-leadership-in-global-health-equity/",
            },
            {
                "label": "East Africa Biodesign Fellowship (EAB)",
                "url": "https://ughe.org/east-africa-biodesign-fellowship",
            },
        ],
    },
    {
        "label": "Research",
        "url": "https://ughe.org/research/",
        "children": [],
    },
    {
        "label": "Centres and Institutes",
        "url": "",
        "children": [
            {
                "label": "Institute of Global Health Equity Research",
                "url": "https://ughe.org/institute-of-global-health-equity-research/",
            },
            {
                "label": "Bill & Joyce Cummings Institute of Global Health",
                "url": "https://ughe.org/bill-and-joyce-cummings-institute-of-global-health/",
            },
            {"label": "Centre for Gender Equity", "url": "https://ughe.org/centre-for-gender-equity/"},
            {"label": "Centre for One Health", "url": "https://ughe.org/centre-for-one-health/"},
            {
                "label": "Centre for Equity in Global Surgery",
                "url": "https://ughe.org/centre-for-equity-in-global-surgery-cegs/",
            },
            {
                "label": "Centre for Population Health",
                "url": "https://ughe.org/centre-for-population-health/",
            },
            {
                "label": "Centre for Leadership in Global Health Equity",
                "url": "https://ughe.org/centre-for-leadership-in-global-health-equity/",
            },
            {"label": "Innovation Centre", "url": "https://ughe.org/innovation-centre-2/"},
            {
                "label": "Centre for Nursing and Midwifery",
                "url": "https://ughe.org/centre-for-nursing-and-midwifery/",
            },
            {
                "label": "Centre for Transformative Learning and Technologies",
                "url": "https://ughe.org/center-for-transformative-learning-technologies-ctlt/",
            },
            {
                "label": "LEAP Centre (Leveraging Equity and Advancement in Practice)",
                "url": "https://ughe.org/leveraging-equity-and-advancement-in-practice-leap/",
            },
        ],
    },
    {
        "label": "Admissions",
        "url": "",
        "children": [
            {"label": "Apply to UGHE", "url": "https://ughe.org/admission/"},
            {
                "label": "Tuition, Fees & Financial Aid (includes Scholarships)",
                "url": "https://ughe.org/tuition-fees-financial-aid/",
            },
            {"label": "I've Been Admitted", "url": "https://ughe.org/ive-been-admitted/"},
            {
                "label": "Mastercard Foundation Scholars Program",
                "url": "https://ughe.org/mastercard-foundation-scholars-program-at-the-university-of-global-health-equity/",
            },
        ],
    },
    {
        "label": "News and Events",
        "url": "",
        "children": [
            {"label": "UGHE Stories", "url": "https://ughe.org/news/"},
            {
                "label": "All UGHE News from start till present",
                "url": "https://ughe.org/news/",
            },
            {"label": "MGHD'21", "url": "https://www.youtube.com/watch?v=E_99Qxjdbdo"},
            {
                "label": "MGHD'23",
                "url": "https://ughe.org/ughe-celebrates-graduation-of-the-8th-cohort-of-the-master-of-science-in-global-health-delivery/",
            },
            {
                "label": "MGHD'24",
                "url": "https://ughe.org/ughe-graduates-shine-at-master-of-science-in-global-health-delivery-commencement/",
            },
            {
                "label": "Women Leaders in Global Health PASHeF I & II",
                "url": "https://ughe.org/women-leaders-in-global-health-conference-2019/",
            },
            {"label": "PASHeF I & II", "url": "https://www.pashef.org/"},
            {"label": "Advancing Medical Education in Africa", "url": "https://www.mededafrica.org/"},
            {"label": "Press releases", "url": "https://ughe.org/press-releases/"},
            {"label": "Newsletters", "url": "https://ughe.org/newsletters/"},
            {
                "label": "UGHE Media Gallery",
                "url": "https://www.flickr.com/photos/183521406@N07/",
            },
        ],
    },
]

SLIDES = [
    {
        "media_type": "image",
        "external_url": "https://ughe.org/wp-content/uploads/2026/07/IMG_2169-scaled.jpg",
        "caption": (
            "The Inaugural Paul E. Farmer Butaro Dialogues: Leaders, partners, "
            "students, and health practitioners gathered at UGHE's Butaro Campus "
            "to advance innovation for maternal and newborn health"
        ),
        "button_label": "Explore more",
        "button_url": "https://ughe.org/butaro-dialogues-ughe-and-partners-call-for-innovation-that-reaches-those-who-need-it-most/",
        "button_color": "#79B9BC",
        "button_text_color": "#FFFFFF",
    },
    {
        "media_type": "image",
        "external_url": "https://ughe.org/wp-content/uploads/2026/04/DSC09176-scaled.jpg",
        "caption": (
            "10 Years of Impact. Dr. Paul Farmer founded UGHE to train the next "
            "generation of global health leaders. A decade on, that work continues "
            "from Butaro."
        ),
        "button_label": "Learn More",
        "button_url": "https://ughe.org/ughe-turns-10/",
        "button_color": "#79B9BC",
        "button_text_color": "#FFFFFF",
    },
    {
        "media_type": "video",
        "external_url": "https://youtu.be/SUd3dZEAlxs",
        "caption": (
            "Experience Our Impact. From classrooms to communities, UGHE is "
            "transforming healthcare across Africa and beyond."
        ),
        "button_label": "Explore more",
        "button_url": "https://www.youtube.com/watch?v=SUd3dZEAlxs",
        "button_color": "#79B9BC",
        "button_text_color": "#FFFFFF",
    },
]

FACTS_TITLE = "Facts & Stats"

STATS = [
    {
        "display_value": "128",
        "description": "Trained community members through UGHE entrepreneurship initiatives",
        "background_color": "#AD3330",
        "text_color": "#FFFFFF",
    },
    {
        "display_value": "1,260",
        "description": "Community members employed for Campus projects",
        "background_color": "#7E2622",
        "text_color": "#FFFFFF",
    },
    {
        "display_value": "677",
        "description": "Leaders across 61 countries trained in our Executive Education since 2016",
        "background_color": "#AD3330",
        "text_color": "#FFFFFF",
    },
    {
        "display_value": "4TH",
        "description": "Among 129 Universities in Sub-Saharan Africa (Times Higher Education Rankings 2024)",
        "background_color": "#7E2622",
        "text_color": "#FFFFFF",
    },
]
