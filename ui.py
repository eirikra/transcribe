import streamlit as st
from utils.transcription import transcribe_with_whisper
from utils.summarization import generate_summary_and_action_points
from utils.formatting import combine_and_format
from utils.diarization import diarize_audio_with_pyannote

# UI Layout
st.title("Transcription and Summarization Tool")
st.write("Upload an audio file to generate a transcript and summary.")

# File Upload
uploaded_file = st.file_uploader("Upload Audio File", type=["wav", "mp3", "m4a"])

# Diarization Option
include_diarization = st.checkbox("Include Speaker Diarization", value=True)

# Process Button
if st.button("Transcribe"):
    if uploaded_file:
        st.write("Processing the audio file... This can take a while.")

        # Save uploaded file
        with open("temp_audio.wav", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Transcription
        transcription = transcribe_with_whisper("temp_audio.wav", model_name="turbo", language="no")

        # Diarization (if selected)
        diarization = None
        if include_diarization:
            st.write("Performing speaker diarization... Please wait.")
            diarization = diarize_audio_with_pyannote("temp_audio.wav", "your_hf_token")

        # Combine and Format
        manuscript = combine_and_format(transcription, diarization, format="markdown")

        # Summary
        st.write("Generating summary and action points... Please wait.")
        summary = generate_summary_and_action_points(manuscript)


        with st.expander("View Summary"):
            st.text_area("Summary", summary, height=500)

        # Display Outputs with Toggles
        with st.expander("View Transcript"):
            st.text_area("Transcript", manuscript, height=500)

        # Download Links
        st.download_button("Download Transcript", manuscript, file_name="transcript.md")
        st.download_button("Download Summary", summary, file_name="summary.txt")
    else:
        st.warning("Please upload an audio file.")
