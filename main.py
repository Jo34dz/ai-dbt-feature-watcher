from fetchers.blog_fetcher import fetch_dbt_blog_entries
from summarizer.llm import summarize_entry
from notifiers.cli_notifier import notify_terminal
from notifiers.slack_notifier import notify_slack
import os
from dotenv import load_dotenv

load_dotenv()  # Loads your .env file with API keys and Slack webhook

def main():
    print("🔎 Checking for new dbt blog posts...")
    entries = fetch_dbt_blog_entries()

    if not entries:
        print("⚠️ No blog entries found.")
        return

    for entry in entries:
        summary = summarize_entry(entry)
        if summary:
            entry["summary"] = summary
            notify_terminal(entry)
            notify_slack(entry)
        else:
            print(f"❌ Could not summarize: {entry['title']}")

if __name__ == "__main__":
    main()
