from pyannote.audio import Pipeline
from dotenv import load_dotenv
import os

load_dotenv()

hf_token = os.getenv("HF_TOKEN")
openai_api_key = os.getenv("OPENAI_API_KEY")

print("Hugging Face Token:", hf_token)
print("OpenAI API Key:", openai_api_key)

try:
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=hf_token)
    print("Pipeline loaded successfully.")
except Exception as e:
    print(f"Failed to load pipeline: {e}")