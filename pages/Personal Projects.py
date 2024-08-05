from pathlib import Path

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image


# ------------ PATH SETTINGS ----------
current_dir = Path(__file__).parent.parent
css_file = current_dir / "styles" / "main.css"


preview_doc_chat = [f"""{current_dir}/assets/personal/doc_chat/{example}""" for example in ['doc_chat_1.png']]
# preview_time_series = [f"""{current_dir}/assets/work/astek/{example}""" for example in ['navigation.png','activity.png','database.png','sensor.png','data.png']]
# preview__llm_chatbot = [f"""{current_dir}/assets/work/alexsys/{example}""" for example in ['home.png','auth.png','add_person.png']]

# ------------ CONSTANTS ----------
PAGE_TITLE = "Personal Projects | Et-tali Mouad"
PAGE_ICON = "🏛"

#-------- PERSONAL PROJECTS CONTENT----------
DOC_CHAT_TITLE = "Chat with Local Documents "
DOC_CHAT_GITHUB = "https://github.com/dibyendutapadar/chat-with-pdf"
DOC_CHAT_ARTICLE = "https://www.linkedin.com/pulse/using-open-source-llms-chat-internal-company-dibyendu-tapadar-5gvyc/?trackingId=W2VGGVoBMUq9gy2eeouJ3g%3D%3D"
DOC_CHAT_APPLINK =""
DOC_CHAT_KEYWORDS = "LLM, RAG, LangChain, document extraction, information retrieval"
DOC_CHAT_STACK = "LLM, RAG (Retrieval-Augmented Generation), LangChain"
DOC_CHAT_DESCRIPTION = """
    - ✔ The project enables chatting and extracting information and insights from internal documents using a locally deployed LLM.
    - 💠 Key Features:
        - 🔸 Uses Retrieval-Augmented Generation (RAG) and LangChain techniques.
        - 🔸 Supports various document formats.
        - 🔸 Provides accurate and context-aware responses based on document content.
    - 💡 The goal is to facilitate efficient and intelligent information retrieval from internal documents.
    """


TIME_SERIES_TITLE = "Time Series Forecasting "
TIME_SERIES_GITHUB = "https://github.com/dibyendutapadar/time-series-forecasting"
TIME_SERIES_ARTICLE = ""
TIME_SERIES_APPLINK ="https://time-series-forecasting-simple.streamlit.app/"
TIME_SERIES_KEYWORDS = "time series, forecasting, SARIMAX, Holt-Winters, Streamlit"
TIME_SERIES_STACK = "SARIMAX, Holt-Winters, Streamlit"
TIME_SERIES_DESCRIPTION = """
    - ✔ The project involves creating a Streamlit app with an intuitive, interactive interface for demand forecasting.
    - 💠 Key Features:
        - 🔸 Utilizes SARIMAX and Holt-Winters methods.
        - 🔸 Allows users to configure parameters and see changes in real-time.
        - 🔸 Provides visualizations of forecasted data.
    - 💡 The goal is to offer an easy-to-use tool for accurate time series forecasting.
    """



LLM_CHATBOT_TITLE = "LLM Driven Agent Chatbot "
LLM_CHATBOT_GITHUB = "https://github.com/dibyendutapadar/streamlit_groq_chatbot"
LLM_CHATBOT_ARTICLE = "https://www.linkedin.com/pulse/experiment-disguise-open-source-llm-hotel-bookings-agent-tapadar-osnfc/?trackingId=4MHsBSaKSWKEEF5VhId3lQ%3D%3D"
LLM_CHATBOT_APPLINK ="https://hotel-chatbot.streamlit.app/"
LLM_CHATBOT_KEYWORDS = "LLM, chatbot, Groq API, hotel booking"
LLM_CHATBOT_STACK = "LLM, Groq API"
LLM_CHATBOT_DESCRIPTION = """
    - ✔ The project involves building a chatbot powered by an LLM to assist guests with information, queries, and bookings.
    - 💠 Key Features:
        - 🔸 Uses Groq API for real-time interactions.
        - 🔸 Acts as a hotel booking agent.
        - 🔸 Provides accurate and context-aware responses.
    - 💡 The goal is to enhance guest experience by providing intelligent and efficient assistance.
    """



DELIVERY_OPTIMIZATION_TITLE = "Delivery Route Optimization "
DELIVERY_OPTIMIZATION_GITHUB = "https://github.com/dibyendutapadar/delivery-routing-optimization"
DELIVERY_OPTIMIZATION_ARTICLE = ""
DELIVERY_OPTIMIZATION_APPLINK ="https://delivery-routing-optimization.streamlit.app/"
DELIVERY_OPTIMIZATION_KEYWORDS = "route optimization, delivery, OR-Tools, Python"
DELIVERY_OPTIMIZATION_STACK = "OR-Tools, Python"
DELIVERY_OPTIMIZATION_DESCRIPTION = """
    - ✔ The project involves creating an application to optimize delivery routes among delivery agents in a city.
    - 💠 Key Features:
        - 🔸 Utilizes OR-Tools for optimization.
        - 🔸 Ensures efficient route planning and resource allocation.
        - 🔸 Reduces delivery time and costs.
    - 💡 The goal is to streamline delivery operations and improve efficiency.
    """


INTERVIEW_SIMULATOR_TITLE = "Interview Simulator "
INTERVIEW_SIMULATOR_GITHUB = ""
INTERVIEW_SIMULATOR_ARTICLE = "https://www.linkedin.com/pulse/introducing-product-management-interview-simulator-custom-tapadar-5d8gc/?trackingId=4MHsBSaKSWKEEF5VhId3lQ%3D%3D"
INTERVIEW_SIMULATOR_APPLINK ="https://chatgpt.com/g/g-xW79GLCbX-mock-product-interview-buddy"
INTERVIEW_SIMULATOR_KEYWORDS = "GPT model, interview simulation, custom prompts, realistic scenarios"
INTERVIEW_SIMULATOR_STACK = "GPT model, custom prompts"
INTERVIEW_SIMULATOR_DESCRIPTION = """
    - ✔ The project involves training a custom GPT model to simulate realistic product interview scenarios.
    - 💠 Key Features:
        - 🔸 Uses specific data, context, and prompts.
        - 🔸 Simulates realistic interview interactions.
    - 💡 The goal is to help candidates prepare effectively for product management interviews.
    """

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")

st.title("Personal Projects")
# --------------- HELPER FUNCTIONS -----------------------

def personal_project_section(PROJECT_TITLE,GITHUB_LINK,ARTICLE_LINK, APP_LINK, PROJECT_KEYWORDS,PROJECT_STACK,PROJECT_DESCRIPTION):

    st.subheader(PROJECT_TITLE)
    st.write('---')
    
    st.write(f'''<span style="color:#f50057; font-size: 15;">**Keywords :**</span> {PROJECT_KEYWORDS}''', unsafe_allow_html=True)

    
    st.write(PROJECT_DESCRIPTION, unsafe_allow_html=True)
    st.write(f'''<span style="color:#f50057; font-size: 15;">**Technologies Used :**</span> {PROJECT_STACK}''', unsafe_allow_html=True)
    if GITHUB_LINK:
        st.write(f"🔗 [GITHUB]({GITHUB_LINK})")
    if ARTICLE_LINK:
        st.write(f"📝[ARTICLE]({ARTICLE_LINK})")
    if APP_LINK:    
        st.write(f"📱[APP LINK]({APP_LINK})")
    st.write('\n')
# ----------- CSS, PDF & Profile Pic SETTINGS --------------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# ------ HERO SECTION -----------

personal_project_section(DOC_CHAT_TITLE, DOC_CHAT_GITHUB, DOC_CHAT_ARTICLE, DOC_CHAT_APPLINK,DOC_CHAT_KEYWORDS, DOC_CHAT_STACK, DOC_CHAT_DESCRIPTION)
with st.expander("**Preview :** "):
    images = [Image.open(image) for image in preview_doc_chat]
    cols = st.columns(len(images))
    for col,image in zip(cols,images):
        with col:
            st.image(image,width=600)


personal_project_section(TIME_SERIES_TITLE, TIME_SERIES_GITHUB, TIME_SERIES_ARTICLE,TIME_SERIES_APPLINK,TIME_SERIES_KEYWORDS, TIME_SERIES_STACK, TIME_SERIES_DESCRIPTION)


personal_project_section(LLM_CHATBOT_TITLE, LLM_CHATBOT_GITHUB, LLM_CHATBOT_ARTICLE,LLM_CHATBOT_APPLINK, LLM_CHATBOT_KEYWORDS, LLM_CHATBOT_STACK, LLM_CHATBOT_DESCRIPTION)


personal_project_section(DELIVERY_OPTIMIZATION_TITLE, DELIVERY_OPTIMIZATION_GITHUB,DELIVERY_OPTIMIZATION_ARTICLE,DELIVERY_OPTIMIZATION_APPLINK, DELIVERY_OPTIMIZATION_KEYWORDS, DELIVERY_OPTIMIZATION_STACK, DELIVERY_OPTIMIZATION_DESCRIPTION)


personal_project_section(INTERVIEW_SIMULATOR_TITLE, INTERVIEW_SIMULATOR_GITHUB, INTERVIEW_SIMULATOR_ARTICLE, INTERVIEW_SIMULATOR_APPLINK, INTERVIEW_SIMULATOR_KEYWORDS, INTERVIEW_SIMULATOR_STACK, INTERVIEW_SIMULATOR_DESCRIPTION)


# #------ Project 4 SECTION
# personal_project_section(E2E_FLASK_PROJECT_TITLE,E2E_FLASK_PROJECT_LINK,E2E_FLASK_PROJECT_KEYWORDS,E2E_FLASK_PROJECT_STACK,E2E_FLASK_PROJECT_DESCRIPTION)
# with st.expander("**Preview of deliverables :** "):
#     st.image(E2E_PIC,width=1000)
# st.write('----')

# #------ Project 4 SECTION
# personal_project_section(THREE_MODELS_PROJECT_TITLE,THREE_MODELS_PROJECT_LINK,THREE_MODELS_PROJECT_KEYWORDS,THREE_MODELS_PROJECT_STACK,THREE_MODELS_PROJECT_DESCRIPTION)
# with st.expander("**Preview of deliverables :** "):
#     st.image(THREE_MODELS_PIC,width=1000)
# st.write('----')