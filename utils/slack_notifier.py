import os
import requests

def post_to_slack(title, link, summary):
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("❌ SLACK_WEBHOOK_URL is not set.")
        return

    message = (
        f"📢 *New dbt Feature:*\n"
        f"📰 *Title:* {title}\n"
        f"🔗 *Link:* {link}\n"
        f"🧠 *Summary:* {summary}"
    )

    response = requests.post(webhook_url, json={"text": message})

    if response.status_code == 200:
        print("✅ Posted to Slack")
    else:
        print(f"⚠️ Slack post failed: {response.status_code} - {response.text}")
