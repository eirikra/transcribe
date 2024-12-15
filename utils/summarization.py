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
    You are a helpful assistant. Summarize the following meeting transcript. Provide:
    1. A concise summary of the discussion.
    2. Key takeaways.
    3. Action points with responsible parties if mentioned.

    Transcript:
    {transcript}

    Output the summary, takeaways, and action points clearly labeled.
    """
    
    # Call GPT API with the correct updated interface
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a summarization assistant."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-4o-mini",  # Or "gpt-3.5-turbo" for lower cost
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
