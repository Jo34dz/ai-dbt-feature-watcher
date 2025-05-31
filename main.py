import os
from dotenv import load_dotenv
from fetchers.blog_fetcher import fetch_dbt_blog_entries
from summarizer.llm import summarize_entry
from notifiers.slack_notifier import post_to_slack
import openai

# load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY")
# if not openai.api_key:
#     print("❌ OPENAI_API_KEY not loaded.")
# else:
#     print("✅ OPENAI_API_KEY loaded.")

# print("🔎 Checking for new dbt blog posts...\n")

# entries = fetch_dbt_blog_entries()[:2]  # Limit for safety; remove limit in production

# for entry in entries:
#     summary = summarize_entry(entry)
#     if summary:
#         message = f"""
# 📢 New dbt Feature:
# 📰 Title: {entry.title}
# 🔗 Link: {entry.link}
# 🧠 Summary: {summary.strip()}
# """
#         post_to_slack(message)
#     else:
#         print(f"❌ Could not summarize: {entry.title}")
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    print("🌐 Testing OpenAI connection...")
    response = openai.models.list()
    print("✅ Connection successful. Available models:")
    for model in response.data[:3]:  # just print 3 models for brevity
        print(f" - {model.id}")
except Exception as e:
    print("❌ Connection to OpenAI failed:")
    print(e)