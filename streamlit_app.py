import streamlit as st
from ai_helper import ask_ai

st.set_page_config(
    page_title="3D Chess Game",
    page_icon="♔",
    layout="wide"
)

st.title("3D Chess Game with Claude AI")

# HTML 파일 렌더링
with open("game.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=1000)

st.sidebar.title("About")
st.sidebar.info("Claude AI를 활용한 3D 체스 게임입니다.")
