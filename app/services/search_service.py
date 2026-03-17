import requests
from bs4 import BeautifulSoup

def fetch_news(sector):
    query = f"{sector} sector India news"
    url = f"https://duckduckgo.com/html/?q={query}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for a in soup.select(".result__a")[:5]:
        results.append({
            "title": a.text,
            "link": a.get("href")
        })

    return results