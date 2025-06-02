import requests

API_KEY = "b109d77c17cc49518172f344a1dada07"

def get_news(category="general"):
    url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()
       

        if data["status"] == "ok":
            articles = data["articles"][:5]  # Limit to 5 headlines
            headlines = [article["title"] for article in articles]
            return headlines
        else:
            return [f"Error from API: {data.get('message', 'Unknown error')}"]
    except Exception as e:
        return [f"Error fetching news: {e}"]

def read_news(command, speak):
    command = command.lower()

    if "tech" in command or "technology" in command:
        category = "technology"
    elif "bollywood" in command or "entertainment" in command or "movie" in command:
        category = "entertainment"
    elif "sports" in command:
        category = "sports"
    elif "business" in command:
        category = "business"
    elif "health" in command:
        category = "health"
    elif "science" in command:
        category = "science"
    elif "world" in command or "india" in command or "indian" in command or "national" in command:
        category = "general"
    else:
        speak("I didn't catch the category. Showing general news.")
        category = "general"

    speak(f"Here are the latest {category} news headlines.")
    headlines = get_news(category)
    if headlines:
        for i, headline in enumerate(headlines, 1):
            speak(f"News {i}: {headline}")
    else:
        speak("Sorry, I couldn't find any news.")
