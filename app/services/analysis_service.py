from app.ai.gemini_client import analyze_with_gemini
from app.services.news_service import get_news

def analyze_sector(sector):
    try:
        news = get_news(sector)
        if not news:
            from app.services.news_service import fetch_news
            news = [n["title"] for n in fetch_news(sector)]
    except:
        from app.services.news_service import fetch_news
        news = [n["title"] for n in fetch_news(sector)]

    try:
        analysis = analyze_with_gemini(sector, news)
        return {
            "status": "success",
            "analysis": analysis,
            "news": news
        }
    except Exception:
        return {
            "status": "error",
            "message": "AI quota exceeded",
            "news": news
        }