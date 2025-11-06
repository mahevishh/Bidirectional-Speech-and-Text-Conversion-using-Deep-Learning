# 🗣️ Bidirectional Speech and Text Conversion using Deep Learning

This project demonstrates a **bidirectional speech-text conversion system** using **deep learning** and **natural language processing (NLP)** techniques.  
It allows users to:

- 🎤 Convert **Speech → Text** using **Wav2Vec2 (by Facebook AI)** — a transformer-based deep learning model trained on 960 hours of audio data.
- 💬 Convert **Text → Speech** using **Google Text-to-Speech (gTTS)** for realistic voice output.

The front end is developed with **Streamlit**, providing an easy-to-use interface where users can upload audio files or record via microphone and receive instant transcriptions or audio playback.

---

### 🚀 Features
- Deep learning–based **speech recognition (ASR)**
- Natural-sounding **text-to-speech generation**
- Real-time microphone input support
- Streamlit-based web UI for interactive experience

---

### 🧠 Technologies Used
- **Python**
- **Hugging Face Transformers**
- **Torch**
- **SoundFile**
- **SpeechRecognition**
- **gTTS**
- **Streamlit**

---

### ⚙️ How It Works
1. The **Wav2Vec2 model** converts audio waveforms into text using a transformer-based architecture.
2. The **gTTS module** converts text into human-like speech and plays it locally.
3. **Streamlit** integrates both features into one clean interface, allowing users to choose between Speech→Text and Text→Speech conversion.

---

### 🧩 Deep Learning Aspect
The deep learning part comes from **Facebook’s Wav2Vec2 model**, which uses **self-supervised learning** on large audio datasets to recognize speech without relying on traditional acoustic models.  
This model understands speech patterns and context directly from waveforms — making it highly accurate and robust.

---

### 💡 Challenges Faced
- Handling audio input/output in Streamlit
- Integrating pretrained models without GPU dependency
- Optimizing latency for real-time speech recognition

---

### 🏁 Outcome
A functional and educational project demonstrating how deep learning can be applied to **Automatic Speech Recognition (ASR)** and **Text-to-Speech (TTS)** systems — a foundation for voice assistants, accessibility tools, and AI-powered communication apps.

---
