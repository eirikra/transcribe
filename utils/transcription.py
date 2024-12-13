# utils/transcription.py
import whisper

def transcribe_with_whisper(audio_file, model_name="base", language="en"):
    """Transcribe audio using Whisper with specified model and language."""
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_file, word_timestamps=True, language=language)
    return result