from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

# ------------ CONSTANTS ----------
PAGE_TITLE = "Academia | Dibyendu Tapadar"
PAGE_ICON = "🏛"
NAME = "Dibyendu Tapadar"


# ---------- PARIS_CITE------------------
PARIS_CITE_ICON = "📜"
PARIS_CITE_TITLE = "**MBA | IIM Ahmedabad**"
PARIS_CITE_PERIOD = "04/2019 - 04/2020"
PARIS_CITE_DESCRIPTION = """
- 🔸 Recipient of the prestigious **All- Round Excellence award**
- 🔸 **Co-Authored:** Futuristic Outlook to Product Management - Industry Review Guide 2019
- 🔸 As part of Profile Committee **Managed and Led** the launch of the Online Portal for the batch Profiles
""" 
# ---------------------------------

# ---------- ESI ------------------
ESI_ICON = "🧑🏻‍💻"
ESI_TITLE = "**BTech in Mechanical Engineering | NIT Durgapur**"
ESI_PERIOD = "06/2008 - 05/20"
ESI_DESCRIPTION = """
""" 
# --------------------------------------

# # ---------- PREP ------------------
# PREP_ICON = "🚀"
# PREP_TITLE = "**Preparatory classes for grand university (Maths/Physics) | Prep School AL-KHANSAA**"
# PREP_PERIOD = "09/2015 - 09/2017"
# PREP_DESCRIPTION = """
# - 🔸 <span style="color:#19A7CE; font-size: 15;">**Relevent Courses:**</span> Mathematics (Linear Algebra, Probabilities, Calculus), Physics, Algorithmic, Phylosophy.
# - 🔸 <span style="color:#19A7CE; font-size: 15;">**Motivation for Prep School :**</span> At this point in life, I didn't know exactly what I wanted to do in life but I knew that prep school was the hardest thing to do after highschool so I chose the hard way.
# - 🔸 <span style="color:#19A7CE; font-size: 15;">**Difficulties :**</span> Adjusting to the level of deep understanding of mathematical concepts especially in calculus for maths and quantum physics in physics
# - 🔸 <span style="color:#19A7CE; font-size: 15;">**What I learned :**</span> I learned that every person has their own pace and talents, some people understand things faster than others. The important thing is to be compassionate and treat people with kindess.
# """ 
# # --------------------------------------

# # ---------- BAC ------------------
# BAC_ICON = "🎒"
# BAC_TITLE = "**Scientific Baccalaureate Mathematical Sciences | Groupe Scholaire Ouhoud**"
# BAC_PERIOD = "06/2015"
# BAC_DESCRIPTION = """
# - 🔸 <span style="color:#19A7CE; font-size: 15;">**Relevent Courses:**</span> Mathematics, Physics, Phylosophy.
# - 🔸 <span style="color:#19A7CE; font-size: 15;">**Difficulties :**</span> The pressure from society to do good in that particular exam, and the expectations of parents and teachers who viewed us as "exellent students who are definitively headed to prep school"
# - 🔸 <span style="color:#19A7CE; font-size: 15;">**What I learned :**</span> All things must come to an end. 
# """ 
# # --------------------------------------

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="centered")


# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent.parent

css_file = current_dir / "styles" / "main.css"

uni_pic = Image.open(current_dir / "assets" / "academic" / "IIMA.jpeg")

esi_pic = Image.open(current_dir / "assets" / "academic" / "IIMA.jpeg")

paris_pic = Image.open(current_dir / "assets" / "academic" / "IIMA.jpeg")

bac_pic = Image.open(current_dir / "assets" / "academic" / "IIMA.jpeg")


st.title("Academic Background")

# --------------- HELPER FUNCTIONS -----------------------
def V_SPACE(lines):
    for _ in range(lines):
        st.write('&nbsp;')

def go_to_full_page(label,page):
    personal_project = st.button(label)
    if personal_project:
        switch_page(page)

def create_background_section(ICON, BACKGROUND_TITLE,BACKGROUND_PERIOD,BACKGROUND_DESCRIPTION):
    st.write('\n')
    st.subheader(BACKGROUND_TITLE)
    st.write(BACKGROUND_PERIOD)
    st.write(BACKGROUND_DESCRIPTION, unsafe_allow_html=True)
    
# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# ------ HERO SECTION -----------
# cols = st.columns(2, gap='small')

# with cols[0]:
#     st.image(uni_pic)


# with cols[1]:
#     st.title(NAME)
#     st.write(DESCRIPTION)


# --------- BACKGROUND ---------
# st.subheader("My Journey 🚩")
# st.write('---')

create_background_section(PARIS_CITE_ICON,PARIS_CITE_TITLE,PARIS_CITE_PERIOD,PARIS_CITE_DESCRIPTION)
V_SPACE(1)
# st.image(paris_pic,width=900, caption="Getting ready for Internships and Job Hunting")
# st.write('----')

create_background_section(ESI_ICON,ESI_TITLE,ESI_PERIOD,ESI_DESCRIPTION)
# st.image(esi_pic, caption="Building connections in Engineering University (I had already finished my turn)")
# st.write('----')

# create_background_section(PREP_ICON,PREP_TITLE,PREP_PERIOD,PREP_DESCRIPTION)
# st.write("""<span style="color:#19A7CE; font-size: 15;">***PS: no picture for prep school period on purpose (if you know you know)*** </span>🙃""",unsafe_allow_html=True)
# st.write('----')

# create_background_section(BAC_ICON,BAC_TITLE,BAC_PERIOD,BAC_DESCRIPTION)
# cols = st.columns(3,gap="small")
# with cols[1]:
#     st.image(bac_pic,caption="Blurry graduation because 2015 Android",width=280)
# st.write('----')


st.write('----')
st.write('----')
st.header("Certifications")