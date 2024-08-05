
from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

from streamlit_pills import pills

# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file = current_dir / "styles" / "main.css"

resume_file = current_dir / "assets" / "cv.pdf"

profile_pic = current_dir / "assets" / "home" /"profile-pic.jpeg"



# ------------ CONSTANTS ----------
PAGE_TITLE = "Portfolio | Dibyendu Tapadar"
PAGE_ICON = ":wave:"
NAME = "Dibyendu Tapadar"
DESCRIPTION = """
Seasoned Product Manager with **10+ years** of total experience, including **7 years in Product Management**. Proven Track Record in **leading cross-functional teams**, fostering **innovation**, **scaling** products, driving **user engagement** and **growth**. 
In addition to my Product Management experience, I have a hands-on proficiency in data science (ML, GenAI) and analytics, building applications to serve industry use cases (check out Personal Projects section)
"""


PROJECTS = """
    - 💠 LLM driven chatbot to interact with local documents (llama3.1, RAG, langchain)
    - 💠 LLM driven chatbot to act as Hotel Booking Agent (Groq API)
    - 💠 Interactive Demand Forecasting using SARIMAX and Holt-Winters (python
    - 💠 Delivery Route Optimization Simulator (Python, Streamlit, OR_Tools)
    - 💠 PM Interview Simulator
    - 💠 This Portfolio
"""

st.set_page_config(
    page_title=PAGE_TITLE, 
    page_icon=PAGE_ICON,
    layout="wide",
    )


st.title("DIBYENDU TAPADAR")
st.write("Product Manager by profession, Data Scientist by passion. Creating Tech for Human Good")

# --------------- HELPER FUNCTIONS -----------------------
def V_SPACE(lines):
    for _ in range(lines):
        st.write('&nbsp;')

def go_to_full_page(label,page):
    personal_project = st.button(label)
    if personal_project:
        switch_page(page)


# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

profile_pic = Image.open(profile_pic)


# ------ HERO SECTION -----------

cols = st.columns([.3, .7], gap='small')

with cols[0]:
    st.image(profile_pic, width=230)


with cols[1]:
    st.write(DESCRIPTION)
    st.download_button( 
        label="📄 Download Resume",
        data= PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )


# -------- SOCIALS ---------


EMAIL = "mailto:x19dibyendu@iima.ac.in"
WHATSAPP = "https://wa.me/+917044090396"
LINKEDIN = "https://www.linkedin.com/in/dibyendu-tapadar/"
GITHUB = "https://github.com/dibyendutapadar"

V_SPACE(1)

col_email, col_whatsapp, col_linkedin, col_github = st.columns(4)

with col_email:
    st.markdown(f'<a href="{EMAIL}" target="_blank">📫 Email me</a>', unsafe_allow_html=True)
with col_whatsapp:
    st.markdown(f'<a href="{WHATSAPP}" target="_blank">💬 Reach out on WhatsApp</a>', unsafe_allow_html=True)
with col_linkedin:
    st.markdown(f'<a href="{LINKEDIN}" target="_blank">🔗 Check out my Linkedin</a>', unsafe_allow_html=True)
with col_github:
    st.markdown(f'<a href="{GITHUB}" target="_blank">💻 Explore my GitHub</a>', unsafe_allow_html=True)



# ------- EXPERIENCE AND QUALIFS --------

V_SPACE(1)
st.subheader('About me 🛝')
st.write(
    """
    - ✔️ **10+ years of total experience**, including 7 years in Product Management, with expertise in data analytics, machine learning, and AI.
    - ✔️ Led cross-functional teams to develop AI-assisted frontend tools and offline test-conducting platforms, achieving significant reductions in UI development time and evaluation turnaround time.
    - ✔️ Managed popular applications in both online and offline mode in EdTech sector, driving user engagement, and reducing operational costs.
    - ✔️ Directed large scale platform integrations
    - ✔️ Managed multiple 0-1 products from inception to launch to scale, across B2B, B2C, internal and platform applications.
    - ✔️ Passionate about creating MVP tools as POC for industrial use cases
    """
,unsafe_allow_html=True)

go_to_full_page("Check out details here" , "Professional Experience")



# --- SKills ---
st.write("---")
st.subheader("Key Skills🔬")
skills = ["End-to-End Product Management", "Strategic Product Planning", "Product Road-Mapping", "0-to-1 Products", 
          "Wireframing & UI/UX Design", "User-Centric Design & Research", "Agile Methodologies", 
          "Cross-Functional Leadership", "Data Analytics", "Machine Learning & Artificial Intelligence", "Generative AI"]
icons = ["🛠️","📈","🗺️","🚀","🎨","🕵️‍♂️","⚡","👥","📊","🧩","🧠"]

selected = pills("",skills ,icons)





# --- Tools ---
st.write("---")
st.subheader("Tools and Technologies`🔬")
st.write(
    """
    - 📊 **Data Analytics & Visualization:** Excel, SQL, Python, Looker, Tableau, Snowflake, PowerBI
    - 🛠️ **Workspace:** Miro, Whimsical, Confluence, Notion
    - 🧪  **Project Management:** Trello, Jira, Aha, Rally
    - 🎨 **Design Tools:** Invision, Balsamiq, Figma, Mockup
    - 💻 **Programming & scripting:** HTML, CSS, JavaScript, PHP, Flutter, Python (Flask, Django, Streamlit)
    - 🧬 **Data Science:** Modeling (Regression, Classification, Forecasting), Exploratory and Predictive Analytics, LLM, Generative AI, LangChain, RAG (Retrieval-Augmented Generation), crew AI
    """
)


st.write("---")
# --- Projects & Accomplishments ---
st.subheader("Personal Projects 🧙‍♂️")


st.write(PROJECTS)

go_to_full_page("Details of Personal Projects" , "Personal Projects")