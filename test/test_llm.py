import sys, os
from dotenv import load_dotenv
load_dotenv()  # 👈 ADD THIS

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from fetchers.blog_fetcher import fetch_dbt_blog_entries
from summarizer.llm import summarize_entry

def test_summarize_blog_entries():
    entries = fetch_dbt_blog_entries()
    print(f"🧪 Testing summarization of {len(entries)} entries...")

    for entry in entries:
        summary = summarize_entry(entry)
        print("\n📰", entry["title"])
        print("🤖 LLM Summary:", summary or "❌ Failed")

if __name__ == "__main__":
    test_summarize_blog_entries()
