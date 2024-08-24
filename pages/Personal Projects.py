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
PAGE_TITLE = "Personal Projects | Dibyendu Tapadar"
PAGE_ICON = "🏛"

#-------- PERSONAL PROJECTS CONTENT----------
ADAPTIVE_LEARNING_TITLE = "Adaptive Learning without question-answer dataset"
ADAPTIVE_LEARNING_GITHUB = "https://github.com/dibyendutapadar/adaptive-learning"
ADAPTIVE_LEARNING_ARTICLE = "https://www.linkedin.com/posts/dibyendu-tapadar_ai-edtech-genai-activity-7232618708748095489-7lRV?utm_source=share&utm_medium=member_desktop"
ADAPTIVE_LEARNING_APPLINK ="https://adaptive-learning.streamlit.app/"
ADAPTIVE_LEARNING_KEYWORDS = "Adaptive learning, llama-index, GenAI, EdTech"
ADAPTIVE_LEARNING_STACK = "Python, Groq, llama-index, llama3.1-8B, SQLite, Streamlit, Pydantic"
ADAPTIVE_LEARNING_DESCRIPTION = """
    - ✔ Generates multiple choice questions based on a students chose topic, grade and proficiency level
    - 💡 How it works
        - Streamlit interface enables the user to to enter grade, topic of interest, current proficiency level (estiamated) and desired proficiency level
        - Inputs are wrapped in a prompt and response is generated through an inference API call. Response is structured through pydantic.
        - Student is asked the question, and based on the answer, the proficiency is updated
        - Interaction data is saved in SQLite table and added as a context to the prompt of the next API call.
        - Proficiency is increased/decreased based on the students response using a statistical model.
    """








IMAGE_ANALYZER_AGENT_TITLE = "Image Analysis with LLaVa and LLaMa"
IMAGE_ANALYZER_AGENT_GITHUB = "https://github.com/dibyendutapadar/ai-agent-image-analyzer"
IMAGE_ANALYZER_AGENT_ARTICLE = "https://www.linkedin.com/posts/dibyendu-tapadar_ai-genai-llm-activity-7227887993305325569-KPB1?utm_source=share&utm_medium=member_desktop"
IMAGE_ANALYZER_AGENT_APPLINK =""
IMAGE_ANALYZER_AGENT_KEYWORDS = "AI Image Analysis, LLaMA, LLAVA, CrewAI, Streamlit, Marketing, EdTech, HealthTech"
IMAGE_ANALYZER_AGENT_STACK = "LLaMA,LLAVA,Ollama CrewAI, Streamlit"
IMAGE_ANALYZER_AGENT_DESCRIPTION = """
    - ✔ Use multiple Local LLMs to analyse images and perform industry specific tasks using crewai
    - 💠 Key Features:
        - 🔸 Insta Influencer
            - Sifts through multiple uplaoded files and prepare detailed description
            - The AI analyzes the chosen images and suggests captions that are not only relevant but also optimized for engagement, considering factors like trending hashtags, current events, and user-provided context."
        - 🔸 EdTech
            - Reads texts and describe images from scanned photos of student answer sheets
            - The AI analyses the answers, provides feedback and marks to each answer
        - 🔸 HealthTech
            - Processes images such as Xray
            - The AI analyses and provides what is wrong with the image, suggested procedures and advice for the patient
    - 💡 How it works
        - Streamlit interface enables the user to upload image(s)
        - LLava multimodal model for image description agent and passes on to the next agent
        - The next agent utilises LLama model to analyse the description and provides output to the user
    """



AI_TRAVEL_AGENT_TITLE = "AI Travel agent for Stay and Itinerary Planning"
AI_TRAVEL_AGENT_GITHUB = "https://github.com/dibyendutapadar/travel-agent-crewai"
AI_TRAVEL_AGENT_ARTICLE = "https://www.linkedin.com/pulse/ai-travel-agent-crewai-ollama-dibyendu-tapadar-dvyxc/?trackingId=gp3S8XR1yjhnsQWQmg39ig%3D%3D"
AI_TRAVEL_AGENT_APPLINK =""
AI_TRAVEL_AGENT_KEYWORDS = "LLM, LangChain, Ollama, crewAI, TreavelTech, OTA"
AI_TRAVEL_AGENT_STACK = "Ollama, CrewAI, Streamlit"
AI_TRAVEL_AGENT_DESCRIPTION = """
    - ✔ Traditional OTAs like MakeMyTrip and Booking often limit users to specific filters and search parameters. Our goal is to provide an unrestricted search experience where users can express their unique travel needs and receive customized suggestions.
    - 💠 Key Features:
        - 🔸 Personalized Search: Use detailed descriptions to find the perfect stay.
            - Example: "A secluded stay by a riverside within 200 km from Bangalore, with high-speed Wi-Fi and parking."
            - Example: "A homestay right on the beach in Goa, within 3000 rupees per night."
        - 🔸 AI-Powered Recommendations: Get tailored travel options based on your inputs.
        - 🔸 Detailed Itineraries: Receive comprehensive travel itineraries based on selected stays and user interests.
    - 💡 How it works
        - Intent Mapper Agent: Extracts key details from the user's travel query.
        - Finder Agent: Searches for suitable travel recommendations.
        - Formatter Agent: Formats the recommendations for the user.
        - Itinerary Maker Agent: Creates detailed travel itineraries
    """



TRAFFIC_SIGNAL_TITLE = "Automated Traffic Signal duration simulator based on real time traffic data"
TRAFFIC_SIGNAL_GITHUB = ""
TRAFFIC_SIGNAL_ARTICLE = "https://dibyendutapadar.wixsite.com/my-site/post/intelligent-traffic-signal-control"
TRAFFIC_SIGNAL_APPLINK ="https://dibyendutapadar.pythonanywhere.com/traffic"
TRAFFIC_SIGNAL_KEYWORDS = "SmartCity, Traffic Signal, Traffic Control, Python"
TRAFFIC_SIGNAL_STACK = "Python, Django, Bing Maps"
TRAFFIC_SIGNAL_DESCRIPTION = """
    - ✔ To address the complexities of traffic signal coordination, I introduce a web application that empowers traffic engineers and city planners to optimize signal durations based on real-time traffic flow data.
    - 💡 How it works
        - 🔸 Interactive Map Selection: Users can select the location of a traffic signal crossing with the help of an interactive Bing Map interface.
        - 🔸 Direction Input: The application guides users through the process of inputting the number of directions traffic flows across the crossing.
        - 🔸 Dynamic Traffic Flow Calculation: The system integrates with bing API to fetch real-time traffic flow data between specified coordinates.
        - 🔸 Result Display: The application presents the calculated signal durations in a clear and concise tabular format.
    """





DOC_CHAT_TITLE = "Chat with Local Documents "
DOC_CHAT_GITHUB = "https://github.com/dibyendutapadar/chat-with-pdf"
DOC_CHAT_ARTICLE = "https://www.linkedin.com/pulse/using-open-source-llms-chat-internal-company-dibyendu-tapadar-5gvyc/?trackingId=W2VGGVoBMUq9gy2eeouJ3g%3D%3D"
DOC_CHAT_APPLINK =""
DOC_CHAT_KEYWORDS = "LLM, RAG, LangChain, document extraction, information retrieval"
DOC_CHAT_STACK = "LLM, RAG (Retrieval-Augmented Generation), LangChain, Streamlit, Ollama"
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
TIME_SERIES_STACK = "SARIMAX, Holt-Winters, Streamlit, Python"
TIME_SERIES_DESCRIPTION = """
    - ✔ The project involves creating a Streamlit app with an intuitive, interactive interface for demand forecasting.
    - 💠 Key Features:
        - 🔸 Utilizes SARIMAX and Holt-Winters methods.
        - 🔸 Allows users to configure parameters and see changes in real-time.
        - 🔸 Provides visualizations of forecasted data.
    - 💡 The goal is to offer an easy-to-use tool for accurate time series forecasting.
    """



LLM_CHATBOT_TITLE = "LLM Driven Hotel Booking Chatbot "
LLM_CHATBOT_GITHUB = "https://github.com/dibyendutapadar/streamlit_groq_chatbot"
LLM_CHATBOT_ARTICLE = "https://www.linkedin.com/pulse/experiment-disguise-open-source-llm-hotel-bookings-agent-tapadar-osnfc/?trackingId=4MHsBSaKSWKEEF5VhId3lQ%3D%3D"
LLM_CHATBOT_APPLINK ="https://hotel-chatbot.streamlit.app/"
LLM_CHATBOT_KEYWORDS = "LLM, chatbot, Groq API, hotel booking"
LLM_CHATBOT_STACK = "LLM, Groq API, Streamlit"
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
DELIVERY_OPTIMIZATION_STACK = "OR-Tools, Python, Streamlit"
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
    st.write('\n')
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

st.write('\n')
personal_project_section(AI_TRAVEL_AGENT_TITLE, AI_TRAVEL_AGENT_GITHUB, AI_TRAVEL_AGENT_ARTICLE,AI_TRAVEL_AGENT_APPLINK,AI_TRAVEL_AGENT_KEYWORDS, AI_TRAVEL_AGENT_STACK, AI_TRAVEL_AGENT_DESCRIPTION)
personal_project_section(IMAGE_ANALYZER_AGENT_TITLE, IMAGE_ANALYZER_AGENT_GITHUB, IMAGE_ANALYZER_AGENT_ARTICLE,IMAGE_ANALYZER_AGENT_APPLINK, IMAGE_ANALYZER_AGENT_KEYWORDS, IMAGE_ANALYZER_AGENT_STACK, IMAGE_ANALYZER_AGENT_DESCRIPTION)
personal_project_section(ADAPTIVE_LEARNING_TITLE, ADAPTIVE_LEARNING_GITHUB, ADAPTIVE_LEARNING_ARTICLE,ADAPTIVE_LEARNING_APPLINK,ADAPTIVE_LEARNING_KEYWORDS, ADAPTIVE_LEARNING_STACK, ADAPTIVE_LEARNING_DESCRIPTION)
personal_project_section(TIME_SERIES_TITLE, TIME_SERIES_GITHUB, TIME_SERIES_ARTICLE,TIME_SERIES_APPLINK,TIME_SERIES_KEYWORDS, TIME_SERIES_STACK, TIME_SERIES_DESCRIPTION)
personal_project_section(LLM_CHATBOT_TITLE, LLM_CHATBOT_GITHUB, LLM_CHATBOT_ARTICLE,LLM_CHATBOT_APPLINK, LLM_CHATBOT_KEYWORDS, LLM_CHATBOT_STACK, LLM_CHATBOT_DESCRIPTION)
personal_project_section(TRAFFIC_SIGNAL_TITLE, TRAFFIC_SIGNAL_GITHUB, TRAFFIC_SIGNAL_ARTICLE,TRAFFIC_SIGNAL_APPLINK, TRAFFIC_SIGNAL_KEYWORDS, TRAFFIC_SIGNAL_STACK, TRAFFIC_SIGNAL_DESCRIPTION)
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