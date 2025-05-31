import os
import requests

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def post_to_slack(message: str):
    if not SLACK_WEBHOOK_URL:
        print("❌ SLACK_WEBHOOK_URL is not set.")
        return False

    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)

    if response.status_code == 200:
        print("✅ Posted to Slack")
        return True
    else:
        print(f"❌ Failed to post to Slack: {response.status_code} - {response.text}")
        return False
