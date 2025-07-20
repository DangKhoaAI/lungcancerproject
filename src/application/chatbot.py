import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

def show_chatbot():
    st.title("🤖 AI Chatbot Hỗ trợ Ung thư phổi")

    st.markdown("""
        Chatbot dưới đây được tích hợp để hỗ trợ người dùng trong việc tìm hiểu, 
        đặt câu hỏi liên quan đến ung thư phổi, triệu chứng, chẩn đoán và phòng ngừa.
    """)

    chatbot_src = os.getenv("CHATBOT_SRC")
    chatbot_html = f"""
    <iframe 
        src="{chatbot_src}"
        style="width: 100%; height: 650px; border: none;">
    </iframe>
    """

    st.markdown(chatbot_html, unsafe_allow_html=True)
