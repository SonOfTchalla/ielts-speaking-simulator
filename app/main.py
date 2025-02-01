import streamlit as st
from speech_to_text import transcribe_audio
from conversational_ai import generate_response
from text_to_speech import speak_text
from scoring import evaluate_response
from feedback import generate_feedback

st.title("IELTS Speaking Simulator")

if "conversation" not in st.session_state:
    st.session_state.conversation = []

for role, text in st.session_state.conversation:
    st.write(f"{role}: {text}")