import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from notifiers.slack_notifier import post_to_slack

message = """
📢 New dbt Feature:
📰 Title: Unlocking analyst-driven data transformation: dbt Canvas is GA
🔗 Link: https://www.getdbt.com/blog/dbt-canvas-is-ga
🧠 Summary: dbt Canvas is now GA and helps analysts visualize, document, and write dbt code more efficiently.
"""

print("🧪 Sending test Slack notification...\n")
post_to_slack(message)
