import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
import os
import google.generativeai as genai

# ✅ Configure Gemini
genai.configure(api_key="AIzaSyCb1C48-tZ3KWcv8nZRs0Txug2vfnsikaw")
model = genai.GenerativeModel('gemini-1.5-flash')

# pip install pocketsphinx google-generativeai

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "3562617c6c524cad9f4ba2b761218487"

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    prompt = (
        "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant. "
        "Give short responses please.\n\n"
        f"User: {command}"
    )
    response = model.generate_content(prompt)
    return response.text.strip()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        parts = c.lower().split(" ")
        if len(parts) >= 2:
            song = parts[1]
            link = musicLibrary.music.get(song)
            if link:
                webbrowser.open(link)
            else:
                speak("Song not found in library.")
        else:
            speak("Please say the song name.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles[:5]:
                speak(article['title'])
        else:
            speak("Sorry, couldn't fetch news.")
    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            print("recognizing...")
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            word = recognizer.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print(f"Error: {e}")
