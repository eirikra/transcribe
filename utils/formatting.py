def combine_and_format(transcription, diarization, format="markdown"):
    """Combine Whisper transcription with Pyannote diarization and format as a manuscript."""
    combined_output = []
    for word in transcription['segments']:
        start_time = word['start']
        end_time = word['end']
        text = word['text']

        # Find the speaker for this word based on diarization timestamps
        speaker = "Unknown"
        for segment, _, spk in diarization.itertracks(yield_label=True):
            if segment.start <= start_time <= segment.end:
                speaker = spk
                break

        combined_output.append({
            "speaker": speaker,
            "start": start_time,
            "end": end_time,
            "text": text
        })

    # Merge consecutive entries by the same speaker
    manuscript = []
    current_speaker = None
    current_text = []
    current_times = []

    for entry in combined_output:
        if entry["speaker"] == current_speaker:
            current_text.append(entry["text"])
            current_times.append(f"{entry['start']:.2f}-{entry['end']:.2f}")
        else:
            if current_speaker is not None:
                time_range = ", ".join(current_times)
                if format == "markdown":
                    manuscript.append(f"**{current_speaker} ({time_range})**:\n{' '.join(current_text)}\n")
                else:
                    manuscript.append(f"[{current_speaker} ({time_range})]: {' '.join(current_text)}")
            current_speaker = entry["speaker"]
            current_text = [entry["text"]]
            current_times = [f"{entry['start']:.2f}-{entry['end']:.2f}"]

    # Append the last speaker's text
    if current_speaker is not None:
        time_range = ", ".join(current_times)
        if format == "markdown":
            manuscript.append(f"**{current_speaker} ({time_range})**:\n{' '.join(current_text)}\n")
        else:
            manuscript.append(f"[{current_speaker} ({time_range})]: {' '.join(current_text)}")

    return "\n\n".join(manuscript)
