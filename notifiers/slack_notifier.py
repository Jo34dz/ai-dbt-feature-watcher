import os
import requests

def notify_slack(entry):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("⚠️ SLACK_WEBHOOK_URL not set in .env")
        return

    message = (
        f"*🆕 dbt Feature Update*\n"
        f"*Title:* {entry['title']}\n"
        f"*Link:* {entry['link']}\n"
        f"*Summary:* {entry['summary']}"
    )

    response = requests.post(
        webhook_url,
        json={"text": message},
        headers={"Content-Type": "application/json"}
    )

    if response.status_code != 200:
        print(f"❌ Failed to post to Slack: {response.status_code}")
    else:
        print("✅ Posted to Slack")
