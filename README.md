# Transcription and Speaker Diarization Tool

## Description
This project provides an end-to-end solution for transcribing audio files, performing speaker diarization, and generating structured manuscripts and summaries. It integrates cutting-edge tools like OpenAI's Whisper for transcription, Pyannote for speaker diarization, and GPT for automated summarization. The tool is designed to streamline documentation and meeting analysis by providing outputs with timestamps, speaker identification, and concise action points.

---

## Features

- **Transcription**: Converts audio to text with word-level timestamps for accuracy.
- **Speaker Diarization**: Identifies and labels individual speakers in the audio.
- **Timestamped Manuscripts**: Combines transcription and diarization into readable documents.
- **Automated Summarization**: Generates summaries, key takeaways, and action points from the transcript.
- **Live Transcription**: Provides real-time transcription capabilities (experimental).
- **Flexible Output Formats**: Supports Markdown and plain text for manuscripts.
- **User Interface**: A lightweight GUI built using Streamlit for ease of use.
- **GPU Acceleration**: Optimized for faster processing with GPU support.

---

## Project Structure

```plaintext
transcribe/
├── main.py                   # Main application logic
├── ui.py                     # Streamlit-based user interface
├── .env                      # Environment variables for API keys
├── requirements.txt          # Python dependencies
├── utils/                    # Helper modules
│   ├── transcription.py      # Whisper transcription logic
│   ├── diarization.py        # Pyannote diarization logic
│   ├── formatting.py         # Combines and formats outputs
│   ├── summarization.py      # GPT-based summarization logic
└── output/                   # Directory for generated manuscripts and summaries
```

---

## Installation

### Prerequisites
- Python 3.8 or higher
- GPU (optional, for faster processing with Pyannote)
- OpenAI API Key (for GPT summarization)
- Hugging Face Token (for Pyannote diarization)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/eirikra/transcribe.git
   cd transcribe
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add API keys to a `.env` file:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   HF_TOKEN=your_huggingface_token
   ```

---

## Usage

### Command-Line Interface (CLI)
1. Run the application:
   ```bash
   python main.py
   ```
2. Provide the required inputs:
   - Path to the audio file.
   - Option to include speaker diarization.

### Graphical User Interface (GUI)
1. Run the Streamlit-based UI:
   ```bash
   streamlit run ui.py
   ```
2. Upload an audio file, choose options for diarization, and generate transcripts and summaries.

---

## Outputs
- **Manuscript**: `[date] [time] - manuscript - [audio-filename].md`
- **Summary**: `[date] [time] - summary - [audio-filename].txt`

---

## Contribution

Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open a discussion first.

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
