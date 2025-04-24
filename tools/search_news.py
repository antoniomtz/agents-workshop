# Import the necessary library
from duckduckgo_search import DDGS

def search_news_by_sentiment(topic: str, sentiment: str, max_results: int = 5):
    """
    Searches for news articles on DuckDuckGo based on a topic and a desired sentiment.

    Args:
        topic: The main subject of the news (e.g., 'bitcoin', 'renewable energy').
        sentiment: The desired sentiment qualifier (e.g., 'positive', 'good', 
                   'negative', 'bad', 'happy', 'friendly', 'optimistic', 'pessimistic').
        max_results: The maximum number of news results to return. Defaults to 5.

    Returns:
        A list of dictionaries, where each dictionary represents a news article
        containing keys like 'date', 'title', 'body', 'url', 'source'.
        Returns an empty list if no results are found or an error occurs.
        The LLM calling this tool is responsible for summarizing the results.
    """
    # Construct a search query combining the topic and sentiment
    query = f"{sentiment} news about {topic}"
    
    print(f"Tool Debug: Searching news with query: '{query}', max_results={max_results}") # For LLM/tool interaction debugging

    try:
        # Use context manager for DDGS object
        with DDGS() as ddgs:
            # Perform the news search
            results = list(ddgs.news(
                keywords=query,
                region='wt-wt',      # Search worldwide
                safesearch='moderate', # Moderate safesearch setting
                timelimit=None,      # Get latest news (no specific time limit like 'd' for day, 'w' for week)
                max_results=max_results
            ))
        
        print(f"Tool Debug: Found {len(results)} news articles.") # For LLM/tool interaction debugging
        
        # Return the list of results (dictionaries)
        return results
    except Exception as e:
        # Print error message if the search fails
        print(f"Tool Error: An error occurred during the DuckDuckGo news search: {e}")
        # Return an empty list in case of an error
        return []

print(search_news_by_sentiment("bitcoin", "positive"))