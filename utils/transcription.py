# utils/transcription.py
import whisper
import functools
import pyaudio
import numpy as np

def transcribe_with_whisper(audio_file, model_name="base", language="en"):
    """Transcribe audio using Whisper with specified model and language."""
    whisper.torch.load = functools.partial(whisper.torch.load, weights_only=True)
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_file, word_timestamps=True, language=language)
    return result


def live_transcribe_with_whisper(model_name="small", language="en", chunk_duration=2):
    """
    Perform live transcription from a microphone using Whisper with improved reliability.
    """
    # Load Whisper model
    model = whisper.load_model(model_name)

    # Setup PyAudio for microphone input
    audio_format = pyaudio.paInt16
    channels = 1
    rate = 16000  # Whisper expects 16 kHz audio
    chunk_size = int(rate * chunk_duration)  # Number of frames per chunk

    audio_interface = pyaudio.PyAudio()
    stream = audio_interface.open(format=audio_format,
                                   channels=channels,
                                   rate=rate,
                                   input=True,
                                   frames_per_buffer=chunk_size)

    print("Listening... (Press Ctrl+C to stop)")
    try:
        while True:
            # Read audio data from the microphone
            audio_data = stream.read(chunk_size, exception_on_overflow=False)
            audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0

            # Transcribe the audio chunk
            try:
                result = model.transcribe(audio_np, language=language)
                print(result["text"])  # Display the transcription in real time
                yield result["text"]  # Stream transcription back to the caller
            except Exception as e:
                print(f"Error during transcription: {e}")
    except KeyboardInterrupt:
        print("Stopping live transcription...")
    finally:
        # Cleanup
        stream.stop_stream()
        stream.close()
        audio_interface.terminate()
