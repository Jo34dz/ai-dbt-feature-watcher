import requests
import feedparser

def fetch_dbt_blog_entries():
    """
    Fetch the latest dbt blog entries from the official RSS feed.
    Returns a list of feedparser entries (limit to 5 for now).
    """
    url = "https://www.getdbt.com/blog/feed.xml"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"⚠️ Failed to fetch blog feed: {e}")
        return []

    feed = feedparser.parse(response.content)
    return feed.entries[:5]  # Return top 5 entries
