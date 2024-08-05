from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image


# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent.parent
css_file = current_dir / "styles" / "main.css"
# AQSONE_PIC_PATH = current_dir / "assets" / "work" / "aqsone" /"aqsone.png"
# ASTEK_PIC_PATH = current_dir / "assets" / "work" /  "astek" / "astek.png"
# ALEXSYS_PIC_PATH = current_dir / "assets" / "work" /  "alexsys" / "alexsys.png"
# DADVISOR_PIC_PATH = current_dir / "assets" / "work" /  "digitaladvisor" / "digitaladvisor.png"


# ------------ CONSTANTS ----------
PAGE_TITLE = "Work Experiences | Dibyendu Tapadar"
PAGE_ICON = "🏛"

#-------- WORK EXPERIENCE CONTENT----------
BRANE_ROLE  = "Sr. Product Manager"
# AQSONE_PIC  = Image.open(AQSONE_PIC_PATH)
BRANE_COMPANY = "Brane Enterprises"
BRANE_PERIOD = "10/2023 - Present"
BRANE_DESCRIPTION = """
        - 💠 Identified the need for an improved and faster UI creation for solutions, proposed and led the development of an <span style="color:##0f0f0f;font-weight: 700;">AI-assisted frontend development tool</span> based on Flutter.
        - 💠 Oversaw the execution with a team of 52 Engineers, and integrated the tool <span style="color:##0f0f0f;font-weight: 700;">(Site-Builder)</span> with the organization’s existing no-code platform.
        - 💠 The tool helped in achieving an <span style="color:##0f0f0f;font-weight: 700;">80% reduction in UI development time</span> enabling creation of visually appealing, responsive and cross-platform supported frontends for the solutions built on the no-code platform.
    """

BYJUS_ROLE  = "Sr. Product Manager"
BYJUS_COMPANY = "BYJUS"
BYJUS_PERIOD = "03/2022 - 10/2023"
BYJUS_DESCRIPTION = """
        - 💠 Orchestrated the development of an <span style="color:##0f0f0f;font-weight: 700;">offline test-conducting platform</span>, powered by an AI-driven personalized tests engine and a module for auto evaluation of pen & paper based answer sheets through computer vision.
        - 💠 The platform successfully catered to 200,000 K-10 students, reducing evaluation turnaround time from 11 days to 2 days, and resulted in an increase of ~5 percentage points in average student scores.
        - 💠 Integrated and automated the internal LMS, CMS, Quiz modules, and the student-facing Learner App, achieving a <span style="color:##0f0f0f;font-weight: 700;">58% reduction in infra costs</span> and an additional reduction of over 3,000 operational man-hours per week.
        - 💠 Accomplished a <span style="color:##0f0f0f;font-weight: 700;">93% reduction in user-reported issues</span> through user story mapping technique.
    """


KHAN_ROLE  = "Sr. Product Manager"
KHAN_COMPANY = "Khan Academy"
KHAN_PERIOD = "12/2020 - 02/2022"
KHAN_DESCRIPTION = """
        - 💠 Drove adoption of the Khan Academy platform in government schools, achieving a <span style="color:##0f0f0f;font-weight: 700;">10-fold increase in monthly active users</span> within a year by developing supplementary products and features.
        - 💠 Engaged over 40,000 teachers across India through the LearnStorm campaign to promote gamified learning, thus boosting engagement and growth.
        - 💠 Partnered with four state education departments, facilitating platform adoption for over 1.5 million users. The most prominent adopter, the state of Punjab, achieved the top position in the National Achievements survey.
    """


MAHINDRA_ROLE  = "Product Manager"
MAHINDRA_COMPANY = "Mahindra Auto Digitech"
MAHINDRA_PERIOD = "02/2016 - 03/2019"
MAHINDRA_DESCRIPTION = """
        - 💠 Launched Carworkz.com, a B2C platform for car servicing, achieving <span style="color:##0f0f0f;font-weight: 700;">4,000+ bookings per month</span> in Mumbai and Pune within six months of launch.
        - 💠 Created DearO, a B2B SaaS solution for streamlining workshop operations, driving customer engagement, invoicing, and inventory management, attracting over <span style="color:##0f0f0f;font-weight: 700;">1,500+ paid users</span> within 6 months of launch.
        - 💠 Recognized with the Mahindra Innovations Award-2018 and Mahindra FUTURise Award 2018 for end-to-end product management of DearO.
    """

TATA_ROLE  = "Assistant Manager"
TATA_COMPANY = "Tata Motors"
TATA_PERIOD = "08/2012 - 01/2016"
TATA_DESCRIPTION = """
        - 💠 Managed profitability and customer satisfaction for 15 franchisee workshops across Punjab and Himachal Pradesh, achieving a <span style="color:##0f0f0f;font-weight: 700;">97% customer satisfaction score</span> per a Nielsen Survey.
        - 💠 Elevated 3 workshops from C-grade to A-grade by implementing targeted quality and profitability improvement initiatives.
    """
# --------------------------------------
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")

st.title("Professional Experiences")

# --------------- HELPER FUNCTIONS -----------------------

def work_experience_section(ROLE,COMPANY,PERIOD,WORK_DESCRIPTION):

    # st.image(PIC,width=150)
    st.subheader(f"**{ROLE} | {COMPANY}**")
    st.write(f"{PERIOD}")
    st.write(WORK_DESCRIPTION, unsafe_allow_html=True)
    

# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# ------ HERO SECTION -----------

# ------ AQSONE SECTION ---------
work_experience_section(BRANE_ROLE,BRANE_COMPANY,BRANE_PERIOD,BRANE_DESCRIPTION)
# with st.expander("**Preview of deliverables :** "):
#     images = [Image.open(image) for image in preview_aqsone]
#     cols = st.columns(len(images))
#     for col,image in zip(cols,images):
#         with col:
#             st.image(image,width=600)
st.write('----')

# BYJUS
work_experience_section(BYJUS_ROLE, BYJUS_COMPANY, BYJUS_PERIOD, BYJUS_DESCRIPTION)
st.write('----')

# Khan Academy
work_experience_section(KHAN_ROLE, KHAN_COMPANY, KHAN_PERIOD, KHAN_DESCRIPTION)
st.write('----')

# Mahindra Auto Digitech
work_experience_section(MAHINDRA_ROLE, MAHINDRA_COMPANY, MAHINDRA_PERIOD, MAHINDRA_DESCRIPTION)
st.write('----')

# Tata Motors
work_experience_section(TATA_ROLE, TATA_COMPANY, TATA_PERIOD, TATA_DESCRIPTION)
st.write('----')

# st.write('----')