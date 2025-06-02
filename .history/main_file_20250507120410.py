import speech_recognition as sr
import webbrowser #inbuilt feature
import pyttsx3
import musiclibrary
#recognitiser class
recognizer=sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c):
  if "open google" in c.lower():
    webbrowser.open("https://google.com")
  elif "open facebook" in c.lower():
     webbrowser.open("https://facebook.com")
  elif "open instagram" in c.lower():
     webbrowser.open("https://instagram.com")
  elif "open linkedin" in c.lower():
    webbrowser.open("https://linkedin.com")
  elif "open youtube" in c.lower():
    webbrowser.open("https://youtube.com")
     elif c.lower().startswith("play"):
        words = c.lower().split(" ")
        if len(words) >= 2:
            song = " ".join(words[1:])
            link = musiclibrary.music.get(song)
            if link:
                speak(f"Playing {song}")
                webbrowser.open(link)
            else:
                speak(f"Sorry, I couldn't find the song {song}")
        else:
            speak("Please say the song name after 'play'")
    else:
        speak("Sorry, I didn't understand that command.")
   
if __name__=="__main__":
  speak("intializing jarvis....")
  while True:
#listen for the word jarvis
      r = sr.Recognizer()
      
       
      print("recognizing...")
# recognize speech using google
    
      try:
          with sr.Microphone() as source:
           print("Listening...")
           audio=r.listen(source,timeout=5,phrase_time_limit=3)
          word=r.recognize_google(audio)
          if(word.lower()=="jarvis"):
           speak("Ya")
           with sr.Microphone() as source:
             print("jarvis active")
             audio=r.listen(source)
             command=r.recognize_google(audio)
             processcommand(command) 
           #listen for command
      except Exception as e:
       print("error; {0}".format(e))

