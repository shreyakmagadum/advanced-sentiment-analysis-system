import streamlit as st
import speech_recognition as sr
from models.sentiment_model import get_sentiment
from models.emotion_model import get_emotion
from models.translator import translate_to_english

st.title("Advanced Sentiment Analysis System")

def load_css():
    with open("static/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

input_type = st.radio("Choose Input Type:", ["Text", "Voice"])

user_input = ""

# TEXT INPUT
if input_type == "Text":
    user_input = st.text_area("Enter your text:")

# VOICE INPUT (WITHOUT pyaudio)
elif input_type == "Voice":
    st.info("Click below and upload an audio file (.wav)")
    audio_file = st.file_uploader("Upload Audio", type=["wav"])

    if audio_file is not None:
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)

        try:
            user_input = r.recognize_google(audio)
            st.success("Recognized Text:")
            st.write(user_input)
        except:
            st.error("Could not process audio")

# PROCESS
if user_input:
    translated_text, lang = translate_to_english(user_input)

    if lang != 'en':
        st.info(f"Translated from {lang}: {translated_text.capitalize()}")

    sentiment = get_sentiment(translated_text)
    emotion = get_emotion(translated_text)

    # 🔥 RULE-BASED CORRECTION
    if emotion.lower() in ["sadness", "anger", "fear"]:
        sentiment = "Negative"
    elif emotion.lower() in ["joy", "love", "surprise"]:
        sentiment = "Positive"

    st.subheader("Analysis Result")
    st.success(f"Sentiment: {sentiment}")
    st.info(f"Emotion: {emotion.capitalize()}")
