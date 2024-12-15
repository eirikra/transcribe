import argparse
import os
from datetime import datetime
from dotenv import load_dotenv
from utils.transcription import transcribe_with_whisper
from utils.diarization import diarize_audio_with_pyannote
from utils.formatting import combine_and_format
from utils.summarization import generate_summary_and_action_points

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

def generate_output_filename(base_name, file_type, output_folder="output"):
    """Generate an output filename based on the date, time, and audio filename in the specified output folder."""
    os.makedirs(output_folder, exist_ok=True)  # Ensure the output folder exists
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(output_folder, f"{timestamp} - {file_type} - {base_name}")

def main():
    print("Loading Hugging Face token...")
    token = load_env_token()

    print("Requesting audio file path...")
    audio_file = get_audio_file()

    print("Would you like to include speaker diarization? (yes/no)")
    include_diarization = input(">>> ").strip().lower() == "yes"

    print("Generating output filename...")
    manuscript_filename = generate_output_filename(audio_file, "manuscript", output_folder="output") + ".md"
    summary_filename = generate_output_filename(audio_file, "summary", output_folder="output") + ".txt"

    print("Transcribing with Whisper...")
    transcription = transcribe_with_whisper(audio_file, model_name="turbo", language="no")

    if include_diarization:
        print("Performing speaker diarization with Pyannote...")
        diarization = diarize_audio_with_pyannote(audio_file, token)
    else:
        diarization = None

    print("Combining transcription and diarization...")
    manuscript = combine_and_format(transcription, diarization, format="markdown")

    print("Generating summary and action points...")
    summary = generate_summary_and_action_points(manuscript)

    # Generate filenames


    # Save manuscript
    print(f"Saving manuscript to {manuscript_filename}...")
    with open(manuscript_filename, "w", encoding="utf-8") as f:
        f.write(manuscript)

    # Save summary
    print(f"Saving summary to {summary_filename}...")
    with open(summary_filename, "w", encoding="utf-8") as f:
        f.write(summary)

    print(f"Process completed. Manuscript saved to '{manuscript_filename}' and summary saved to '{summary_filename}'.")

if __name__ == "__main__":
    main()