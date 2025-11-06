# speech_to_text.py
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
import soundfile as sf

# Load pretrained model and processor once
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

def speech_to_text(audio_path):
    speech, rate = sf.read(audio_path)
    inputs = processor(speech, sampling_rate=rate, return_tensors="pt", padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    pred_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(pred_ids[0])
    return transcription.lower()
