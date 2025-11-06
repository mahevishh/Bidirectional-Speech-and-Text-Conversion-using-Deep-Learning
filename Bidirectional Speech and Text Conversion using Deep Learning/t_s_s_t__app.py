# app.py

import streamlit as st
import tempfile
import base64
import os
import sys
import speech_recognition as sr

# Add current folder to Python path so imports work even with spaces
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Import functions from your main script
from bidirectional_speech_text import speech_to_text, text_to_speech

st.set_page_config(page_title="Bidirectional Speech ↔ Text", page_icon="🗣️")
st.title("🗣️ Bidirectional Speech ↔ Text Conversion using Deep Learning")

option = st.radio("Select Conversion Type:", ["Speech to Text", "Text to Speech"])

# --- SPEECH TO TEXT ---
if option == "Speech to Text":
    st.subheader("🎙️ Convert Speech to Text")

    mode = st.radio("Choose Input Method:", ["Use Microphone", "Upload Audio File"])

    if mode == "Use Microphone":
        st.info("Click 'Start Recording' and speak clearly.")
        if st.button("🎤 Start Recording"):
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                st.write("Listening...")
                audio_data = recognizer.listen(source)
                st.write("Recognizing...")
                try:
                    text = recognizer.recognize_google(audio_data)
                    st.success("✅ Speech Recognized:")
                    st.write(text)
                except sr.UnknownValueError:
                    st.error("Sorry, I could not understand your speech.")
                except sr.RequestError:
                    st.error("API unavailable or connection error.")

    elif mode == "Upload Audio File":
        audio_file = st.file_uploader("Upload an audio file", type=["wav"])
        if audio_file is not None:
            with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
                temp_audio.write(audio_file.read())
                text = speech_to_text(temp_audio.name)
                st.subheader("📝 Transcribed Text:")
                st.write(text)

# --- TEXT TO SPEECH ---
elif option == "Text to Speech":
    st.subheader("💬 Convert Text to Speech")
    user_text = st.text_area("Enter text to convert to speech:")
    if st.button("🔊 Convert to Speech"):
        output_path = text_to_speech(user_text)
        if output_path:
            audio_file = open(output_path, "rb").read()
            st.audio(audio_file, format="audio/mp3")
