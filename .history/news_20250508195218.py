# news.py
import requests

API_KEY = "b109d77c17cc49518172f344a1dada07"

def get_news(category="general"):
   GET https://newsapi.org/v2/top-headlines?country=us&apiKey=A
    try:
        response = requests.get(url)
        data = response.json()

        if data["status"] == "ok":
            articles = data["articles"][:5]  # Limit to 5 headlines
            headlines = [article["title"] for article in articles]
            return headlines
        else:
            return []
    except Exception as e:
         return [f"Error fetching news: {e}"]

def read_news(command,speak):
    if "tech" in command:
        category = "technology"
    elif "bollywood" in command or "entertainment" in command:
        category = "entertainment"
    elif "world" in command:
        category = "general"
    elif "india" in command:
        category = "general"
    else:
        category = "general"

    speak(f"Here are the latest {category} news headlines.")
    headlines = get_news(category)
    if headlines:
        for i, headline in enumerate(headlines, 1):
            speak(f"News {i}: {headline}")
    else:
        speak("Sorry, I couldn't find any news.")
