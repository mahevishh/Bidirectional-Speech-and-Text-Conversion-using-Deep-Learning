# text_to_speech.py
from gtts import gTTS
import os

def text_to_speech(text):
    if not text:
        raise ValueError("No text provided!")
    output_path = "output.wav"
    tts = gTTS(text=text, lang='en')
    tts.save(output_path)
    print("Speech generated successfully!")
    return output_path
