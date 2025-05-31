import os
from openai import OpenAI, OpenAIError

# Load your OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in environment variables.")

client = OpenAI(api_key=api_key)

def summarize_entry(entry):
    """
    Summarizes a dbt blog entry using OpenAI.
    Returns a string summary or None if it fails.
    """
    prompt = (
        f"Summarize the following dbt blog post for a Slack update:\n\n"
        f"Title: {entry.get('title')}\n"
        f"Link: {entry.get('link')}\n"
        f"Summary:\n"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()

    except OpenAIError as e:
        print(f"⚠️ Error summarizing entry: {e}")
        return None
