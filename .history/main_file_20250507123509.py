import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import musiclibrary

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Optional: Personalize voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)  # 0 for male, 1 for female

def speak(text):
    print("Novia:", text)
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
            speak("You were silent. Try again.")
        except Exception as e:
            speak(f"Error: {e}")
    return ""

def play_song(song_name):
    link = musiclibrary.music.get(song_name)
    if link:
        speak(f"Playing {song_name}")
        webbrowser.open(link)
    else:
        speak(f"I couldn't find the song '{song_name}'.")

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
    elif command.startswith("play"):
        parts = command.split()
        if len(parts) > 1:
            song_name = " ".join(parts[1:])
            play_song(song_name)
        else:
            speak("Please say the name of the song.")
    elif "stop" in command or "exit" in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("Sorry, I don't recognize that command.")

if __name__ == "__main__":
    speak("Hi, I'm Novia, your assistant. Say 'Nova' to activate me.")
    while True:
        wake_word = listen()
        if "nova" in wake_word:
            speak("I'm listening.")
            command = listen("What would you like me to do?")
            if command:
                process_command(command)
