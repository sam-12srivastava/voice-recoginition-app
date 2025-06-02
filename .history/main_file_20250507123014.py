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