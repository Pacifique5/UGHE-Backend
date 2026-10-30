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
    "footer_heading": "Connect With Us",
    "footer_background_color": "#C22226",
    "footer_text_color": "#FFFFFF",
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
        "count_to": 128,
        "count_suffix": "",
        "count_duration_ms": 2000,
        "use_grouping": True,
        "background_color": "#C42127",
        "text_color": "#FFFFFF",
    },
    {
        "display_value": "1,260",
        "description": "Community members employed for Campus projects",
        "count_to": 1260,
        "count_suffix": "",
        "count_duration_ms": 2000,
        "use_grouping": True,
        "background_color": "#8F1A1D",
        "text_color": "#FFFFFF",
    },
    {
        "display_value": "677",
        "description": "Leaders across 61 countries trained in our Executive Education since 2016",
        "count_to": 677,
        "count_suffix": "",
        "count_duration_ms": 2000,
        "use_grouping": True,
        "background_color": "#C42127",
        "text_color": "#FFFFFF",
    },
    {
        "display_value": "4TH",
        "description": "Among 129 Universities in Sub-Saharan Africa (Times Higher Education Rankings 2024)",
        "count_to": 4,
        "count_suffix": "TH",
        "count_duration_ms": 100,
        "use_grouping": False,
        "background_color": "#8F1A1D",
        "text_color": "#FFFFFF",
    },
]

ACADEMICS_IMAGE = "https://ughe.org/wp-content/uploads/2026/04/53929621747_e41fdfdf78_o-scaled.jpg"
IMPACT_IMAGE = "https://ughe.org/wp-content/uploads/2026/04/UGHE-buildings--scaled.jpg"

LANDING_BLOCKS = [
    {
        "kind": "promo",
        "title": "Applications Are Open",
        "body": (
            "Applications are now open for Bachelor of Medicine, Bachelor of Surgery – "
            "Master of Science in Global Health Delivery (MBBS-MGHD). This 6.5-year "
            "integrated dual degree programme prepares the next generation of "
            "clinician-leaders to address health challenges at every level."
        ),
        "button_label": "Learn More and Apply Now",
        "button_url": "https://ughe.org/admission-for-mbbs-mghd-program/",
        "image_url": "https://youtu.be/SUd3dZEAlxs",
        "background_color": "#111111",
        "overlay_color": "#C42127B0",
        "text_color": "#FFFFFF",
        "button_color": "#FFFFFF",
        "button_text_color": "#C42127",
        "group_key": "",
    },
    {
        "kind": "feature",
        "title": "Explore Academics",
        "body": (
            "Classrooms that thrive in vibrant discourse, based on cases that demand "
            "real world answers and applications"
        ),
        "button_label": "Learn more about academics",
        "button_url": "https://ughe.org/academics/",
        "image_url": ACADEMICS_IMAGE,
        "background_color": "#000000",
        "overlay_color": "#00000030",
        "text_color": "#FFFFFF",
        "button_color": "#FFFFFF",
        "button_text_color": "#C42127",
        "group_key": "academics",
    },
    {
        "kind": "feature",
        "title": "Study at UGHE",
        "body": (
            "Welcome to a next-generation university where you will have the freedom to "
            "create and then pursue your own academic goals. At University of Global "
            "Health Equity, we empower students to make the most of their ideas through "
            "hands-on education and intentional collaboration."
        ),
        "button_label": "About admission",
        "button_url": "https://ughe.org/admission/",
        "image_url": "",
        "background_color": "#000000",
        "overlay_color": "#C4212730",
        "text_color": "#FFFFFF",
        "button_color": "#FFFFFF",
        "button_text_color": "#C42127",
        "group_key": "academics",
    },
    {
        "kind": "news",
        "title": "News & Updates",
        "body": "",
        "button_label": "View all news",
        "button_url": "https://ughe.org/news-and-events/",
        "image_url": "",
        "background_color": "#F5F5F5",
        "overlay_color": "#F5F5F5",
        "text_color": "#111111",
        "button_color": "#C42127",
        "button_text_color": "#FFFFFF",
        "group_key": "",
    },
    {
        "kind": "impact",
        "title": "Experience Our Impact",
        "body": (
            "From classrooms to communities, UGHE is transforming healthcare across "
            "Africa and beyond. Watch our medical students, faculty and leadership "
            "discuss the vision driving change."
        ),
        "button_label": "Watch here",
        "button_url": "https://www.youtube.com/watch?v=M2l7sCuOnHo",
        "image_url": IMPACT_IMAGE,
        "background_color": "#000000",
        "overlay_color": "#00000099",
        "text_color": "#FFFFFF",
        "button_color": "#FFFFFF",
        "button_text_color": "#C42127",
        "group_key": "",
    },
]

NEWS_STORIES = [
    {
        "title": "Walking Toward a Future Without Podoconiosis",
        "url": "https://ughe.org/walking-toward-a-future-without-podoconiosis/",
        "image_url": "https://ughe.org/wp-content/uploads/2026/08/55325793932_50dfe2e107_k-480x320.jpg",
        "category": "Centre for One Health",
        "category_url": "https://ughe.org/category/centre-for-one-health/",
    },
    {
        "title": "Full recovery from trauma is not only about surviving the injury",
        "url": "https://ughe.org/full-recovery-from-trauma-is-not-only-about-surviving-the-injury/",
        "image_url": "https://ughe.org/wp-content/uploads/2026/08/202605327_Kibogora_Equi-InjuryWorkshop_DNA_4-scaled-480x320.jpg",
        "category": "Alumni",
        "category_url": "https://ughe.org/category/alumni/",
    },
    {
        "title": "Butaro Dialogues: UGHE and Partners Call for Innovation That Reaches Those Who Need It Most",
        "url": "https://ughe.org/butaro-dialogues-ughe-and-partners-call-for-innovation-that-reaches-those-who-need-it-most/",
        "image_url": "https://ughe.org/wp-content/uploads/2026/07/IMG_2169-scaled-480x320.jpg",
        "category": "News",
        "category_url": "https://ughe.org/category/news/",
    },
    {
        "title": "UGHE hosts “Tumenye Kaminuza”, a Campus Open Day to Strengthen Community Engagement",
        "url": "https://ughe.org/ughe-hosts-tumenye-kaminuza-a-campus-open-day-to-strengthen-community-engagement/",
        "image_url": "https://ughe.org/wp-content/uploads/2026/07/Tumenye-Kaminuza-480x320.jpg",
        "category": "Campus Operations and Campus Life",
        "category_url": "https://ughe.org/category/campus-operations-and-campus-life/",
    },
    {
        "title": "More Than Access: How Three Scholars Are Redefining What Global Health Looks Like",
        "url": "https://ughe.org/more-than-access-how-three-scholars-are-redefining-what-global-health-looks-like/",
        "image_url": "https://ughe.org/wp-content/uploads/2026/06/Collage-for-MF-480x320.png",
        "category": "Spotlight",
        "category_url": "https://ughe.org/category/spotlight/",
    },
    {
        "title": "UGHE Ranks Fifth Globally in Medicine for Planetary Health",
        "url": "https://ughe.org/ughe-ranks-fifth-globally-in-medicine-for-planetary-health/",
        "image_url": "https://ughe.org/wp-content/uploads/2026/05/2024_ughe_onehealth_fieldschool_pmugemana1504_53707441807_o-1-scaled-480x320.jpg",
        "category": "News",
        "category_url": "https://ughe.org/category/news/",
    },
    {
        "title": "Accompaniment in Action: The Nursing and Midwifery Week",
        "url": "https://ughe.org/accompaniment-in-action-the-nursing-and-midwifery-week/",
        "image_url": "https://ughe.org/wp-content/uploads/2026/05/55269586520_bb7163c180_5k-scaled-480x320.jpg",
        "category": "Centre for Nursing and Midwifery",
        "category_url": "https://ughe.org/category/centre-for-nursing-and-midwifery/",
    },
    {
        "title": "UGHE at CUGH 2026: Research and Awards",
        "url": "https://ughe.org/ughe-at-cugh-2026-research-and-awards/",
        "image_url": "https://ughe.org/wp-content/uploads/2026/05/Featured-image-480x320.jpg",
        "category": "News",
        "category_url": "https://ughe.org/category/news/",
    },
    {
        "title": "UGHE Announces Dr. Sheila Davis as the first Professor of Practice",
        "url": "https://ughe.org/ughe-announces-dr-sheila-davis-as-the-first-professor-of-practice/",
        "image_url": "https://ughe.org/wp-content/uploads/2026/04/Sheila-Davis-2-scaled-480x320.jpg",
        "category": "Leadership",
        "category_url": "https://ughe.org/category/leadership/",
    },
    {
        "title": "Scaling High-Quality Health Professional Education in Rural Rwanda and Beyond",
        "url": "https://ughe.org/scaling-high-quality-health-professional-education-in-rural-rwanda-and-beyond/",
        "image_url": "https://ughe.org/wp-content/uploads/2026/04/DSC09176-scaled-480x320.jpg",
        "category": "News",
        "category_url": "https://ughe.org/category/news/",
    },
]

FOOTER_OFFICES = [
    {
        "body": (
            "Butaro, Burera, Rwanda\n"
            "Office Hours: 8:00 a.m. – 5:00 p.m.\n"
            "+250 786 405 072\n"
            "info@ughe.org"
        ),
    },
    {
        "body": (
            "Kigali Admin office:\n"
            "KG 7 Ave, Kigali Heights, 5th Floor, East Wing\n"
            "P.O. Box 6955"
        ),
    },
]

SOCIAL_LINKS = [
    {"label": "Facebook", "url": "https://www.facebook.com/ughe.org"},
    {"label": "X", "url": "https://twitter.com/ughe_org"},
    {"label": "Instagram", "url": "https://www.instagram.com/ughe_org/"},
    {"label": "LinkedIn", "url": "https://www.linkedin.com/company/university-of-global-health-equity"},
]
