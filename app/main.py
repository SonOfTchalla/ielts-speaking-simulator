import streamlit as st
from speech_to_text import transcribe_audio
from conversational_ai import generate_response
from text_to_speech import speak_text
from scoring import evaluate_response
from feedback import generate_feedback

# Streamlit app
st.title("IELTS Speaking Simulator")

# Initialize session state
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Display conversation
for role, text in st.session_state.conversation:
    st.write(f"{role}: {text}")

# Record user input
if st.button("Start Speaking"):
    user_input = transcribe_audio()
    st.session_state.conversation.append(("User", user_input))

    # Generate AI response
    ai_response = generate_response(user_input)
    st.session_state.conversation.append(("Examiner", ai_response))

    # Speak AI response
    speak_text(ai_response)

    # Evaluate and provide feedback
    scores = evaluate_response(user_input)
    feedback = generate_feedback(user_input, scores)
    st.write("Feedback:", feedback)