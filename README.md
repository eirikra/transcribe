# Transcription and Speaker Diarization Tool

## Description
This project automates the transcription and diarization of audio files, providing structured manuscripts with timestamps and speaker identification. Additionally, it generates summaries, key takeaways, and action points from the content for efficient post-meeting documentation. The tool leverages OpenAI's Whisper for transcription, Pyannote for speaker diarization, and GPT for summarization.

---

## Features
- **Transcription**: Converts audio to text with high accuracy, including word-level timestamps.
- **Speaker Diarization**: Identifies and labels individual speakers in the audio.
- **Timestamped Manuscripts**: Combines transcription and diarization into a readable manuscript with timestamps.
- **Automated Summarization**: Generates concise summaries, key takeaways, and action points from the transcript.
- **Flexible Output Formats**: Supports Markdown and plain text for manuscripts.
- **GPU Acceleration**: Optimized for faster processing on systems with GPUs.

---

## Project Structure

```
transcription_tool/
├── main.py                   # Main entry point for the application
├── .env                      # Environment variables file (API keys)
├── requirements.txt          # Python dependencies
├── utils/
│   ├── transcription.py      # Whisper transcription logic
│   ├── diarization.py        # Pyannote diarization logic
│   ├── formatting.py         # Combines and formats the output
│   ├── summarization.py      # GPT summarization logic
└── output/                   # Directory for generated manuscripts and summaries
```

---

## Installation

### Prerequisites
- Python 3.8 or higher
- GPU (optional, for faster processing with Pyannote)
- OpenAI API Key (for GPT-based summarization)
- Hugging Face Token (for Pyannote diarization)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd transcription_tool
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
4. Add your API keys to a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   HF_TOKEN=your_huggingface_token
   ```

---

## Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Provide the required inputs**:
   - Enter the path to the audio file when prompted.

3. **Outputs**:
   - A manuscript with timestamps and speaker labels.
   - A summary with key takeaways and action points.

The files will be saved in the following format:
- Manuscript: `[date] [time] - manuscript - [audio-filename].txt`
- Summary: `[date] [time] - summary - [audio-filename].txt`

---

## Example

### Input
Audio File: `meeting.wav`

### Outputs
**Manuscript** (Markdown):
```
**Speaker 1 (0:00-1:15)**:
Hello, everyone. Let's review the project updates.

**Speaker 2 (1:16-2:45)**:
Sure, here are the latest details.
```

**Summary**:
```
**Summary**:
The team discussed project updates and assigned responsibilities.

**Key Takeaways**:
1. Project milestones are on track.
2. Additional resources may be needed for upcoming tasks.

**Action Points**:
1. [John] Finalize the project report by next Monday.
2. [Alice] Coordinate with the marketing team for updates.
```

---

## Development Roadmap
- **Real-Time Transcription**: Support for live audio inputs.
- **Improved Summarization**: Fine-tune prompts for context-specific outputs.
- **Web Interface**: A GUI for non-technical users to upload files and retrieve outputs.
- **Cloud Deployment**: Host the tool on a cloud platform for broader accessibility.

---

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

---

## Acknowledgements
- [OpenAI Whisper](https://github.com/openai/whisper) for transcription.
- [Pyannote.audio](https://github.com/pyannote/pyannote-audio) for diarization.
- [OpenAI GPT](https://platform.openai.com/docs) for summarization.

