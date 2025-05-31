import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_entry(entry):
    prompt = (
        f"Summarize this blog post in 1-2 concise sentences for internal changelog readers:\n\n"
        f"Title: {entry['title']}\n"
        f"Summary: {entry['summary']}\n"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or gpt-3.5-turbo
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"⚠️ Error summarizing entry: {e}")
        return None
