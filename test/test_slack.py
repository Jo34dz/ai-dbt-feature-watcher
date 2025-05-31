import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.slack_notifier import post_to_slack

# Debug print
print("🧪 DEBUG: SLACK_WEBHOOK_URL =", os.environ.get('SLACK_WEBHOOK_URL'))

# TEMP fallback (replace with your actual webhook)
if not os.environ.get("SLACK_WEBHOOK_URL"):
    os.environ["SLACK_WEBHOOK_URL"] = "https://hooks.slack.com/services/XXX/YYY/ZZZ"

# Post
post_to_slack(
    title="Test: dbt Copilot Alert",
    link="https://example.com/dbt-copilot",
    summary="This is a test summary sent directly from your dbt Feature Watcher."
)
