import datetime
import os
import smtplib
import sys
import time
import webbrowser
import speech_recognition as sr
import instaloader
import pyaudio
# from Alarm import alarm
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import requests

import wikipedia
from requests import get
import threading
# from Personal import *
# import wolframalpha

#Wolfarm_app = wolframalpha.Client(WolfarnId)

friend = pyttsx3.init()
voices = friend.getProperty('voices')
friend.setProperty('voice', voices[1].id)




# Text to speech
def speak(audio):
    friend.say(audio)
    friend.runAndWait()


# Convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query.lower()



        except sr.WaitTimeoutError:
            speak("Sorry, I didn't hear anything. Please try again.")
            return "none"

        except sr.UnknownValueError:
            print("UnknownValueError: Unable to recognize speech.")
            speak("Sorry, I couldn't understand what you said. Please try again.")
            return "none"

        except sr.RequestError as e:
            print(f"RequestError: Could not request results from Google Speech Recognition service; {e}")
            speak("Sorry, an error occurred while processing your request. Please try again later.")
            return "none"

        except Exception as e:
            print(e)
            speak("Sorry, an error occurred. Please try again.")
            return "none"





# Greet the user
def wish():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    tt = time.strftime(("%I:%M %p"))
    print(tt)
    if 0 <= hour < 12:
        speak(f"Good Morning Sir, its {tt}")
    elif 12 <= hour < 18:
        speak(f"Good Afternoon Sir, its {tt}")
    else:
        speak(f"Good Evening Sir, its {tt}")
    speak("I am kabad , an Artificial intelligence, created by Gaurav Kumar. Please tell me how can I help you, Did you have any qestion? ")



# Send Email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gauravkumarbairwa25@gmail.com', 'gauravkumarbairwa')
    server.sendmail('gauravkumarbairwa25@gmail.com', to, content)
    server.close()


def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=0265a7c64b094f69af06c8678b873271"

    main_page = requests.get(main_url).json()

    articles = main_page["articles"]

    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seven", "eighth", "nine", "tenth"]

    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        print(head[i])
        speak((f"today's {day[i]} news is: {head[i]}"))
        # print(head[i])

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for alarm time...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            timing = r.recognize_google(audio, language='en-in')
            print(f"User said: {timing}")
            return timing.lower()
        except sr.WaitTimeoutError:
            speak("Sorry, I didn't hear the time. Please try again.")
            return "none"
        except Exception as e:
            print(e)
            speak("Sorry, an error occurred. Please try again.")
            return "none"


if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()
        # Logic building for tasks
        if "open notepad" in query:
            path = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(path)
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "play music" in query:
            music_dir = "C:\\Users\\user\\Music"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            print(f"Your IP address is {ip}")
            speak(f"Your IP address is {ip}")
        elif "wikipedia" in query:
            speak("Searching Wikipedia.......")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("www.youtube.com")
        elif "open facebook" in query:
            speak("Opening Facebook")
            webbrowser.open("www.facebook.com")
        elif "open stack overflow" in query:
            speak("Opening Stack Overflow")
            webbrowser.open("www.stackoverflow.com")
        elif "open google" in query:
            speak("Opening Google")
            speak("Sir, what should I search on Google?")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        elif "play my song on youtube" in query:
            pywhatkit.playonyt("Luis Fonsi - Despacito ft. Daddy Yankee")
        elif "play my video on youtube" in query:
            pywhatkit.playonyt("https://www.youtube.com/watch?v=rgGDTO8g2Pg&t=3894s&ab_channel=PrathamTaneja")
        elif "no thanks" in query:
            speak("Thanks for using Me sir, have a good day")
            sys.exit()
            speak("Sir, do you have any other work to ask me?")
        elif "close notepad" in query:
            speak("Okay sir, closing Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close command prompt" in query:
            speak("Okay sir, closing cmd")
            os.system("taskkill /f /im cmd.exe")
        elif "tell me a joke" in query:
            joke = pyjokes.get_jokes(category='neutral', language='en')
            print(joke)
            speak(joke)
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif "tell me the news" in query:
            speak("please wait sir, fetching the latest news")
            news()
        elif "give me the news" in query:
            speak("please wait sir, fetching the latest news")
            news()

        elif "open" in query:
            from Dictapp import openappweb

            openappweb(query)

        elif "close" in query:
            from Dictapp import closeappweb

            closeappweb(query)

        elif "set an alarm" in query:
            speak("Alright! Set it for When?")
            Timing = Listen()
            Timing = str(Timing).replace(".", "")
            Timing = Timing.upper()
            threading.Thread(target=alarm, args=[Timing]).start()
        # elif "who are you" or "how are you" or "what your name" or "name" in query:
        #            print("I'm an AI created by OpenAI called ChatGPT. You can think of me as a conversational assistant here to help answer your questions, chat, or assist you with anything you need. How can I assist you today?")
        #            speak("I'm an AI created by Gaurav kumar called Kajal. You can think of me as a conversational assistant here to help answer your questions, chat, or assist you with anything you need. How can I assist you today?")
        #
        # else:
        #     try:
        #         ans = Wolfarm_Alpha()
        #
        #     except Exception as e:
        #         pass

        elif  "where i am" in query:
            speak("Wait sir,let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text

                url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()

                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir , i think we are in{city} city of{country}country")
            except Exception as e:
                speak("Sorry sir ,Due to network issue i am not able to find where we are"  )
                pass


        elif "instagram profile" in query:
            speak("i am opening your  account")
            name = "sadiesink_"
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir here is the profile of your {name}")
            time.sleep(1)
            speak("sir would you like to download profile picture")

            condition = takecommand().lower()
            print(condition)
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name,profile_pic_only=True)
                speak("Done sir")
            else:
                pass

        # elif "take screenshot" in query:
        #     speak("sir ,pl")

        elif "take screenshot" in query:
            speak("sir ,plese tell me the name for this screeshot file")
            name = takecommand().lower()
            speak("please hold the screen for few seconds")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Done sir")