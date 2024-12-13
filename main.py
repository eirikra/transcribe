import argparse
import os
from datetime import datetime
from dotenv import load_dotenv
from utils.transcription import transcribe_with_whisper
from utils.diarization import diarize_audio_with_pyannote
from utils.formatting import combine_and_format

def load_env_token():
    """Load the Hugging Face token from a .env file."""
    load_dotenv()  # Load environment variables from .env file
    token = os.getenv("HF_TOKEN")
    if not token:
        raise ValueError("Hugging Face token not found. Please set the 'HF_TOKEN' variable in the .env file.")
    return token

def get_audio_file():
    """Prompt the user to input the path to the audio file."""
    audio_file = input("Enter the path to the audio file: ").strip()
    if not os.path.isfile(audio_file):
        raise FileNotFoundError(f"The file '{audio_file}' does not exist.")
    return audio_file

def generate_output_filename(audio_file):
    """Generate an output filename based on the date, time, and audio filename."""
    base_name = os.path.splitext(os.path.basename(audio_file))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_transcript_{timestamp}.txt"

def main():
    print("Loading Hugging Face token...")
    token = load_env_token()

    print("Requesting audio file path...")
    audio_file = get_audio_file()

    print("Generating output filename...")
    output_file = generate_output_filename(audio_file)

    print("Transcribing with Whisper...")
    transcription = transcribe_with_whisper(audio_file, model_name="turbo", language="no")

    print("Performing speaker diarization with Pyannote...")
    diarization = diarize_audio_with_pyannote(audio_file, token)

    print("Combining transcription and diarization...")
    manuscript = combine_and_format(transcription, diarization)

    print(f"Saving manuscript to {output_file}...")
    with open(output_file, "w") as f:
        f.write(manuscript)

    print(f"Process completed. Manuscript saved to '{output_file}'.")

if __name__ == "__main__":
    main()