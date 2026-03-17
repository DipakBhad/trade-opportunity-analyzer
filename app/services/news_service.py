import requests

NEWS_API_KEY = "4a2a22a358d64a1b9fd669cc7d094502"

def get_news(sector):
    url = f"https://newsapi.org/v2/everything?q={sector}&apiKey={NEWS_API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    articles = data.get("articles", [])[:5]

    news_list = []
    for article in articles:
        news_list.append(article["title"])

    return news_list