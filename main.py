import os
from dotenv import load_dotenv
from fetchers.blog_fetcher import fetch_dbt_blog_entries
from summarizer.llm import summarize_entry
from notifiers.slack_notifier import post_to_slack

load_dotenv()

print("🔎 Checking for new dbt blog posts...\n")

entries = fetch_dbt_blog_entries()[:2]  # Limit for safety; remove limit in production

for entry in entries:
    summary = summarize_entry(entry)
    if summary:
        message = f"""
📢 New dbt Feature:
📰 Title: {entry.title}
🔗 Link: {entry.link}
🧠 Summary: {summary.strip()}
"""
        post_to_slack(message)
    else:
        print(f"❌ Could not summarize: {entry.title}")
