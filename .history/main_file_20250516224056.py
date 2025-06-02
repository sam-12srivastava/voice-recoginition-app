import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import media  # your custom media dictionary
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
            speak("Sorry, I didn't catch that.")
        except sr.WaitTimeoutError:
            pass
        except Exception as e:
            speak(f"Error: {e}")
    return ""

def play_media(name):
   name = name.strip().lower()
   for category, items in media.media.items():
      for title, link in items.items():
        if name == title.lower():
            speak(f"Playing {category.capitalize()} > {title}")
            webbrowser.open(link)
            return
   speak(f"I couldn't find '{name}'. Searching on YouTube.")
   webbrowser.open(f"https://www.youtube.com/results?search_query={name}")

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
    # Add more categories as needed
    read_news(topic, speak)

     elif command.startswith("play"):
        parts = command.split("play", 1)
        if len(parts) > 1:
            item = parts[1].strip()
            play_media(item)
        else:
            speak("Please say the name of what you want to play.")
    elif "stop" in command or "exit" in command:
        speak("Goodbye! Have a great day.")
        return False
    #else:
       # speak("Sorry, I don't recognize that command.")
    return True

# MAIN LOOP
if __name__ == "__main__":
    speak("Hi, I'm Nova, your assistant. Say 'Nova' to activate me.")
    while True:  # Outer loop waits for "nova"
        wake_word = listen()
        if "nova" in wake_word:
            speak("I'm listening. What would you like me to do?")
            while True:  # Inner loop processes commands until "stop"/"exit"
                command = listen()
                if command:
                    should_continue = process_command(command)
                    if not should_continue:
                        break  # Breaks out of inner loop, returns to waiting for "nova"
