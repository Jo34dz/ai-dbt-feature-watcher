def fetch_dbt_blog_entries():
    """
    Static mock for dbt blog posts.
    Replace with real Selenium fetcher later if needed.
    """
    return [
        {
            "source": "blog",
            "title": "Introducing dbt Copilot",
            "link": "https://www.getdbt.com/blog/dbt-copilot-is-ga",
            "published": "2024-05-15",
            "summary": "dbt Copilot is an AI assistant that helps you write models, tests, and documentation using natural language."
        },
        {
            "source": "blog",
            "title": "The Modern Data Stack is Dead. Long Live the Metrics Layer.",
            "link": "https://www.getdbt.com/blog/the-modern-data-stack-is-dead",
            "published": "2024-04-30",
            "summary": "dbt Labs introduces new features to support the Semantic Layer and unify metrics across BI tools."
        }
    ]
