from langchain_core.tools import tool
from tavily import TavilyClient

from app.config.settings import settings


client = TavilyClient(
    api_key=settings.TAVILY_API_KEY
)


@tool
def web_search(query: str) -> str:
    """
    Search the web for up-to-date information.

    Args:
        query: Search query.

    Returns:
        Relevant search results.
    """

    try:
        response = client.search(
            query=query,
            max_results=5
        )

        results = []

        for item in response.get("results", []):
            results.append(
                f"Title: {item.get('title')}\n"
                f"URL: {item.get('url')}\n"
                f"Content: {item.get('content')}\n"
            )

        return "\n---\n".join(results)

    except Exception as e:
        return f"Search error: {str(e)}"