import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fetchers.blog_fetcher import fetch_dbt_blog_entries

def test_blog_fetcher():
    entries = fetch_dbt_blog_entries()
    print(f"✅ Found {len(entries)} blog entries.")
    if entries:
        entry = entries[0]
        print("📰 Title:", entry["title"])
        print("📅 Published:", entry["published"])
        print("🔗 Link:", entry["link"])
        print("📝 Summary Preview:", entry["summary"][:100], "...")
    else:
        print("⚠️ No blog entries found.")

if __name__ == "__main__":
    test_blog_fetcher()
