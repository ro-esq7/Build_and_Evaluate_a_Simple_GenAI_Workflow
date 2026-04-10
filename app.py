# Import Libraries
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Load the API key from the local .env file
load_dotenv()

# Load the API key from the local .env file
api_key = os.getenv("gemini_api_key")
if not api_key:
    raise ValueError("Missing gemini_api_key in your .env file.")

# Build the instruction block that tells the model what to do
# Updated this over time based on the test cases & output quality
system_prompt = """
You are a professional business writing assistant.
Your task is to rewrite rough notes or drafts into a clear, well-structured, and appropriate email.

Requirements:
- Preserve the user's meaning and intent.
- Match the tone to the context of the message.
- For formal or external business messages, use a polished and professional tone.
- For internal, friendly, or social workplace messages, use a warm and natural tone without sounding overly formal.
- Do not invent facts, details, names, subject lines, placeholders, timelines, or other information that were not provided.
- Keep the message concise unless the input clearly requires more detail.
- Include a brief greeting and courteous closing when appropriate.
- Output only the final email draft.
"""

# Output file for saving the generated email draft locally
output_file = "output_email.txt"

# Define a function the calls the API key, inputs the user's rough draft, and makes 3 total attempst if there is a system overload, 
    # and delivers the final output
def generate_email_draft(user_input: str) -> str:
    """Send rough notes to the model and return a polished email draft."""
    import time

    api_key = os.getenv("gemini_api_key")
    if not api_key:
        raise ValueError("Missing gemini_api_key in your .env file.")

    client = genai.Client(api_key=api_key)
    full_prompt = f"{system_prompt}\n\nRough Notes:\n{user_input}"

    last_error = None

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=full_prompt,
            )
            return response.text.strip()
        except Exception as e:
            last_error = e
            if attempt < 2:
                print(f"Attempt {attempt + 1} failed. Trying again in 5 seconds...")
                time.sleep(5)

    raise last_error

# Define a function to save the agent's output to a file
def save_output(text: str, filename: str = output_file) -> None:
    """Save generated email to a text file."""
    Path(filename).write_text(text, encoding="utf-8")

# Define a function that prompts the user to add their rough draft
    # then generates the output and a file to save
    # this function also explicitly states the error if it errors
def main():
    print("\nGenAI Email Drafting Prototype")
    print("-" * 35)
    user_input = input("Paste Your Rough Draft Here:\n> ").strip()

    if not user_input:
        print("No input provided. Closing.")
        return

    try:
        draft = generate_email_draft(user_input)

        print("\nGenerated Email Draft")
        print("-" * 35)
        print(draft)

        save_output(draft)
        print(f"\nDraft also saved to: {output_file}")

    except Exception as e:
        print(f"\nError: {e}")

# Run the app when this file is executed directly
if __name__ == "__main__":
    main()