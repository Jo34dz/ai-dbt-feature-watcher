import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fetchers.blog_fetcher import fetch_dbt_blog_entries
from summarizer.llm import summarize_entry

print("🧪 Testing summarization of 2 entries...\n")

entries = fetch_dbt_blog_entries()[:2]

for entry in entries:
    print(f"📰 {entry.title}")
    summary = summarize_entry(entry)
    if summary:
        print(f"🤖 LLM Summary: {summary}\n")
    else:
        print(f"❌ Failed to summarize: {entry.title}\n")
