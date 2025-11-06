# bidirectional_speech_text.py

import speech_recognition as sr
from gtts import gTTS
import os

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)
        print("Recognizing...")

        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
        except sr.RequestError:
            print("API unavailable or connection error.")
        return None

def text_to_speech(text):
    if not text:
        print("No text provided!")
        return None
    tts = gTTS(text=text, lang='en')
    output_path = "output.mp3"
    tts.save(output_path)
    os.system("start output.mp3")
    print("Speech generated successfully!")
    return output_path

if __name__ == "__main__":
    print(" Speech  Text\n. Text Speech")
    choice = input("Choose an option (1/2): ")

    if choice == '1':
        speech_to_text()
    elif choice == '2':
        text = input("Enter text: ")
        text_to_speech(text)
    else:
        print("Invalid choice!")
