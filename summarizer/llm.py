import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_entry(entry):
    prompt = (
        f"Summarize this dbt blog post in 1–2 sentences:\n\n"
        f"Title: {entry.get('title')}\n"
        f"Link: {entry.get('link')}\n"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        print(f"⚠️ Error summarizing entry: {e}")
        return None
