import speech_recognition as sr
import pyttsx3
import webbrowser
import os
from datetime import datetime
import requests
from media import media
 # your custom media dictionary
from news import read_news
# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()   
engine = pyttsx3.init()

# Set voice: 0 for male, 1 for female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    print("Nova:", text)
    engine.say(text)
    engine.runAndWait()

def listen(prompt=None):
    with sr.Microphone() as source:
        if prompt:
            speak(prompt)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Didn't catch that.")
        except sr.WaitTimeoutError:
            pass
        except Exception as e:
            speak(f"Error: {e}")
    return ""

def play_media(name):
    name = name.strip().lower()
    found = False
    for category, items in media.items():
        for title, link in items.items():
            print(f"Checking {title.lower()} against {name}")
            if name == title.lower():
                found = True
                speak(f"Playing {category.capitalize()} > {title}")
                webbrowser.open(link)
                return
    if not found:
        speak(f"I couldn't find '{name}'. Searching on YouTube.")
        webbrowser.open(f"https://www.youtube.com/results?search_query={name}")
''''''
def play_media(name):

   name = name.strip().lower()

   for category, items in media.items():

      for title, link in items.items():

        if title.lower() in name:

            speak(f"Playing {category.capitalize()} > {title}")

            webbrowser.open(link)

            return

   speak(f"I couldn't find '{name}'. Searching on YouTube.")

   webbrowser.open(f"https://www.youtube.com/results?search_query={name}")
'''
def get_weather(city):
    api_key = "720e50349255afc8cd6d50910d6f1a50"  # 🔁 Replace this with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            speak(f"The temperature in {city} is {temp} degrees Celsius with {description}.")
        else:
            speak("Sorry, I couldn't fetch the weather for that city.")
    except Exception as e:
        speak(f"Error while fetching weather: {e}")

def process_command(command):
    if "google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook.")
    elif "linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn.")
    elif "time" in command:
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")
    elif "news" in command:
      topic = ""
      if "indian" in command:
        topic = "indian"
      elif "world" in command:
        topic = "world"
      elif "sports" in command:
        topic = "sports"
      else:
        topic = "general"  
    # Add more categories as needed
      read_news(topic, speak)
    elif "weather" in command:
        speak("Please say the city name.")
        city = ""
        attempts = 0
        while not city and attempts < 2:
            city = listen()
            attempts += 1
            if not city:
                speak("I didn't hear the city name. Please try again.")
        if city:
            get_weather(city)
        else:
            speak("Still didn't get it. Let's try later.")
  
    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif "calculator" in command:
        speak("Opening Calculator")
        os.system("calc")
    elif "vs code" in command or "visual studio code" in command:
        speak("Opening Visual Studio Code")
        os.system("code")
    elif "paint" in command:
        speak("Opening Paint")
        os.system("mspaint")
    elif "stop" in command or "exit" in command:
        speak("Goodbye! Have a great day.")
        return False
    
    #else:
       # speak("Sorry, I don't recognize that command.")
    return True


# MAIN LOOP
if __name__ == "__main__":
    speak("Hi, I'm Nova, your assistant. Say 'Nova' to activate me.")
    active = True
    while True:  # Outer loop waits for "nova"
     if active:
            wake_word = listen()
            if "nova" in wake_word:
                speak("I'm listening. What would you like me to do?")
                while True:
                    command = listen()
                    if command:
                        should_continue = process_command(command)
                        if not should_continue:
                            active = False
                            break  # exit inner loop, go inactive
     else:
            print("Waiting for wake word...")
            wake_word = listen()
            if "nova" in wake_word:
                speak("I'm back. What would you like me to do?")
                active = True 