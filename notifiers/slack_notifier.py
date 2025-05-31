import os
import requests

def post_to_slack(title, link, summary):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("❌ SLACK_WEBHOOK_URL not found in environment variables.")
        return

    payload = {
        "text": f"\ud83d\udce2 *{title}*\n\ud83d\udd17 {link}\n\ud83e\udde0 {summary}"
    }

    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print("\u2705 Successfully posted to Slack.")
        else:
            print(f"❌ Failed to post to Slack. Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"❌ Exception while posting to Slack: {str(e)}")
