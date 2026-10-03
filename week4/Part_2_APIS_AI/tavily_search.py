# scripts/tavily_search.py

from config import TAVILY_API_KEY
from tavily import TavilyClient

client = TavilyClient(
    api_key=TAVILY_API_KEY
)


def search_link(link):
    response = client.crawl(
        url=link,
        instructions="find contact info, address, hours, fees, eligibility, languages, how to book for Ottawa residents only. ",
        extract_depth="advanced",
        exclude_paths=[ "/blog",
            "/news",
            "/careers",
            "/jobs",
            "/donate",
            "/privacy",
            "/terms",
            "/login",
            "/signup",
            "/register",
            "/account",]
            )
    return(response)