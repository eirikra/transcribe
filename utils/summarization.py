from dotenv import load_dotenv
import os
from openai import OpenAI

# Load .env variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Check if API key is loaded
if not api_key:
    raise ValueError("OpenAI API key not found. Please add it to the .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def generate_summary_and_action_points(transcript):
    """
    Generate a summary, key takeaways, and action points from the transcript.
    """
    # Construct a structured prompt
    prompt = f"""
    You are a highly skilled AI tasked with summarizing a conversation transcript. Your goal is to provide a clear and concise summary that captures the essence of the discussion, highlights key takeaways, identifies action points, and suggests follow-up questions. Additionally, you will include your own reflections on the topics discussed, offering deeper insights or perspectives.

    Output Structure:

    Summary of the Conversation:

    Provide a concise overview of the main topics discussed in the conversation.
    Clearly outline the key points raised, any significant conclusions, or decisions made.
    Key Takeaways:

    Highlight the most critical pieces of information or insights from the conversation.
    Mention any agreed-upon priorities or areas of alignment among the participants.
    Action Points:

    List actionable tasks or steps identified during the discussion.
    Clearly assign ownership (if mentioned in the transcript) and include deadlines or timelines where applicable.
    Follow-Up Questions:

    Pose thoughtful questions to help drill deeper into the topics discussed.
    Ensure these questions are specific, actionable, and tied to unresolved issues or areas needing clarification.
    Reflections:

    Offer your own reflections or analysis of the topics discussed.
    Highlight potential risks, opportunities, or areas where additional focus might be valuable.
    Provide suggestions or alternative perspectives based on your understanding.
    Instructions for Summarizing:

    Be concise yet thorough, ensuring the summary is easy to understand without losing important details.
    Avoid repetition and use professional, neutral language.
    If any part of the transcript is unclear or ambiguous, make note of this in the summary and suggest clarification questions.
    Formatting:
    Use bullet points and headers to organize the output. Avoid long paragraphs. Make it scannable and professional.

    The summary must be written in Norwegian.

    Transcript:
    {transcript}
    """
    
    # Call GPT API with the correct updated interface
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a summarization assistant."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-4o",  # Or "gpt-3.5-turbo" for lower cost
    )
    
    # Extract content
    completion = response.choices[0].message.content
    return completion

def main():
    transcript = """Speaker 1: Hello, everyone. Today's meeting is about the upcoming project milestones. Speaker 2: Sure, let's dive into the details."""
    summary = generate_summary_and_action_points(transcript)
    print("Generated Summary and Action Points:")
    print(summary)

if __name__ == "__main__":
    main()
