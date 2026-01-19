import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/ask"

st.set_page_config(page_title="SafeSpace AI Therapist", layout="wide")
st.title("🧠 SafeSpace – AI Mental Health Therapist")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("What's on your mind today?")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    try:
        response = requests.post(
            BACKEND_URL,
            json={"message": user_input},
            timeout=10
        )
        data = response.json()

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": data.get("response", "I'm here with you.")
        })

    except Exception:
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": "I’m having trouble connecting, but you’re not alone."
        })

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
