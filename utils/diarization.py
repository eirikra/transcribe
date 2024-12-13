# utils/diarization.py
from pyannote.audio import Pipeline
from tqdm import tqdm
import torch

def diarize_audio_with_pyannote(audio_file, hf_token):
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=hf_token)
    if torch.cuda.is_available():
        print(f"Using GPU: {torch.cuda.get_device_name(0)}")
    else:
        print("Using CPU for diarization.")
    
    with tqdm(total=100, desc="Processing Diarization") as pbar:
        diarization = pipeline(audio_file)
        pbar.update(100)
    return diarization
