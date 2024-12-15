# utils/diarization.py
from pyannote.audio import Pipeline
import torch

def diarize_audio_with_pyannote(audio_file, hf_token):
    
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1", use_auth_token=hf_token)

    if torch.cuda.is_available():
        print(f"Using GPU: {torch.cuda.get_device_name(0)}")
    else:
        print("Using CPU for diarization.")
    
    diarization = pipeline(audio_file)
    return diarization
