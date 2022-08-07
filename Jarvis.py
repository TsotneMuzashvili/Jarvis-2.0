from contextlib import nullcontext
from multiprocessing.connection import wait
from unittest import result
from urllib import request
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
from datetime import date
import time
import os
import requests
import keyboard
from keyboard import press
from keyboard import press_and_release
from keyboard import write
import pywhatkit
import random
import wikipedia
import bs4
from bs4 import BeautifulSoup
import pyjokes
import subprocess
import functools
from functools import cache
import PyPDF2
import playsound
from playsound import playsound
import gtts
from gtts import gTTS









today = date.today()



engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



@cache










def speak(text):
    engine.say(text)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("time now is")
    speak(Time)

def date():
    d2 = today.strftime("%B %d, %Y")
    speak("today is")
    speak(d2)

def wishme():
    speak("Jarvis is now open")
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning sir!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon sir!")
    elif hour >=18 and hour<24:
        speak("Good Evening sir!")
    else:
        speak("Good Night sir!")

    speak("i am happy to see you again")
    speak("how can i help you?")

def end():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("wish you Good Morning sir! see you later, if u need somthing i am here")
    elif hour >=12 and hour<18:
        speak("wish you Good Afternoon sir! see you later, if u need somthing i am here")
    elif hour >=18 and hour<24:
        speak("wish you Good Evening sir! see you later, if u need somthing i am here")
    else:
        speak("wish you Good Night sir! see you later, if u need somthing i am here")

def reminder():
    hour = datetime.datetime.now().hour
    if hour >=8 and hour<9:
        speak("Good Morning sir, Wake up!")
    elif hour >=9 and hour<10:
        speak("get ready for todays day sir, this day will be amazing")
    elif hour >=10 and hour<12:
        speak("no reminder sir, you are free")
    elif hour >=12 and hour<13:
        speak("read some book sir, it's good for your brain")
    elif hour >=14 and hour<16:
        speak("it's worckout time sir, u need to get big!")
    elif hour >=17 and hour<20:
        speak("free time with family")
    elif hour >=20 and hour<23:
        speak("no reminder sir, you are free")
    elif hour>=23 and hour<24:
        speak("it's sleep time sir, u should go to sleep")

def news():
    main_url = 'https://newsapi.org/v2/everything?domains=wsj.com&apiKey=094ee193b1514c5cb2b3eeb5ee593595'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "secound", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "thenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

  

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in-geo')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("i didnt hear you, please say that again")
            return "none"
        return statement











if __name__ == '__main__':

    wishme()



    while True:
        statement = takeCommand().lower()

        if statement==0:
            continue

        if "you are free" in statement or "sleep" in statement:
            end()
            break

        elif "hello jarvis" in statement:
            speak("hello sir, how are you?")
            speak("how can i help you sir?")

        elif "how are you" in statement:
            speak("i am fine sir, how are you?")
            speak("how can i help you sir?")

        elif "i am fine" in statement or "i am good" in statement:
            speak("i am happy for you")
            speak("how can i help you sir?")

        elif "time" in statement or "tell me time" in statement:
            time()
            speak("how can i help you sir?")

        elif "date" in statement or "tell me date" in statement:
            date()
            speak("how can i help you sir?")

        elif "reminder" in statement:
            reminder()
            speak("how can i help you sir?")

        elif "news" in statement or "tell me news" in statement:
            speak("this is latest news")
            news()
            speak("how can i help you sir?")

        elif "joke" in statement:
            speak("okey master, i have good joke for you, get ready")
            joke = pyjokes.get_joke()
            speak(joke)
            speak("how can i help you sir?")

        elif 'weather' in statement or 'temperature' in statement:
            search = "temperature in rustavi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")
            speak("how can i help you sir?")

        elif "chrome" in statement or "open chrome" in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("google is now open, what do u want to do?")
            speak("how can i help you sir?")

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.google.com/gmail")
            speak("Google Mail is open now")
            speak("how can i help you sir?")

        elif 'open facebook' in statement:
            webbrowser.open_new_tab("https://www.facebook.com")
            speak("Facebook is open now")
            speak("how can i help you sir?")

        elif 'shop mymarket' in statement or 'mymarket' in statement:
            webbrowser.open_new_tab("https://www.mymarket.ge")
            speak("good shoping in mymarket master")
            speak("how can i help you sir?")

        elif 'shop newegg' in statement or 'newegg' in statement or 'new egg' in statement:
            webbrowser.open_new_tab("https://www.newegg.com")
            speak("good shoping in newegg master")
            speak("how can i help you sir?")

        elif 'shop amazon' in statement or 'amazon' in statement:
            webbrowser.open_new_tab("https://www.amazon.com")
            speak("good shoping in amazon master")
            speak("how can i help you sir?")

        elif "github" in statement:
            webbrowser.open_new_tab('https://github.com/TsotneMuzashvili')
            speak("github is now open")
            speak("how can i help you sir?")

        elif "open the 48 laws of power book" in statement or "open the laws of power book" in statement:
            webbrowser.open_new_tab("file:///C:/Users/snaka/Documents/The_48_Laws_of_Power.pdf")
            speak("the 48 laws of power book is now open")
            speak("how can i help you sir?")

        elif "open calculator" in statement:
            subprocess.call('calc.exe')
            speak("calculator is open now")
            speak("how can i help you sir?")

        elif "close calculator" in statement:
            speak("okey sir, closing calculator")
            os.system("taskkill /f /im calc.exe")
            speak("how can i help you sir?")

        elif "open notepad" in statement:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            speak("notepad is now open")
            speak("how can i help you sir?")

        elif "close notepad" in statement:
            speak("okey sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")
            speak("how can i help you sir?")

        elif "open discord" in statement:
            discordpath = "C:\\Users\\snaka\\AppData\\Local\\Discord\\Update.exe"
            os.startfile(discordpath)
            speak("discord is now open")
            speak("how can i help you sir?")

        elif "close discord" in statement:
            speak("okey sir, closing discord")
            os.system("taskkill /f /im Update.exe")
            speak("how can i help you sir?")

        elif "open firefox" in statement:
            ffpath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(ffpath)
            speak("firefox is now open")
            speak("how can i help you sir?")

        elif "close firefox" in statement:
            speak("okey sir, closing firefox")
            os.system("taskkill /f /im firefox.exe")
            speak("how can i help you sir?")

        elif "open vscode" in statement or "open visual studio code" in statement or "vscode" in statement or "visual studio code" in statement:
            vscpath = "C:\\Users\\snaka\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscpath)
            speak("visual studio code is now open")
            speak("how can i help you sir?")

        elif "close vscode" in statement or "close visual studio code" in statement:
            speak("okey sir, closing visual studio code")
            os.system("taskkill /f /im Code.exe")
            speak("how can i help you sir?")

        elif 'new tab' in statement:

            press_and_release('ctrl + t')
            speak("how can i help you sir?")

        elif 'close tab' in statement:

            press_and_release('ctrl + w')
            speak("how can i help you sir?")

        elif 'new window' in statement:

            press_and_release('ctrl + n')
            speak("how can i help you sir?")

        elif 'history' in statement:

            press_and_release('ctrl + h')
            speak("how can i help you sir?")

        elif 'downloads' in statement:

            press_and_release('ctrl + j')
            speak("how can i help you sir?")

        elif 'switch tab' in statement:

            tab = statement.replace("switch tab ", "")
            Tab = tab.replace("to","")
        
            num = Tab

            bb = f'ctrl + {num}'

            press_and_release(bb)

            speak("how can i help you sir?")

        elif "play music" in statement:
            musicdir = "C:\Tsotne\music"
            songs = os.listdir(musicdir)
            rd = random.choice(songs)
            os.startfile(os.path.join(musicdir, rd))
            speak("how can i help you sir?")

        elif "search" in statement or "google search" in statement:
            import wikipedia as googlescrap

            statement = statement.replace("jarvis", "")
            statement = statement.replace("goole search", "")
            statement = statement.replace("google", "")
            speak("this is what i found on the web!")
            pywhatkit.search(statement)

            result = googlescrap.summary(statement, 3)
            speak(result)
            speak("how can i help you sir?")

        elif "search in wiki" in statement or "search in wikipedia" in statement or "info from wiki" in statement or "information from wikipedia" in statement:
            info = wikipedia.summary(statement)
            speak(info)
            speak("how can i help you sir?")

        elif "play on youtube" in statement or "play youtube video" in statement:
            play = pywhatkit.playonyt(statement)
            speak("youtube video is now playing")
            speak("how can i help you sir?")

        elif 'home screen' in statement:

            press_and_release('windows + m')
            speak("how can i help you sir?")

        elif 'minimize' in statement:

            press_and_release('windows + m')
            speak("how can i help you sir?")

        elif 'show start' in statement:

            press('windows')
            speak("how can i help you sir?")

        elif 'open setting' in statement:

            press_and_release('windows + i')
            speak("how can i help you sir?")

        elif 'open search' in statement:

            press_and_release('windows + s')
            speak("how can i help you sir?")

        elif 'screen shot' in statement:

            press_and_release('windows + SHIFT + s')
            speak("how can i help you sir?")

        elif 'restore windows' in  statement:

            press_and_release('Windows + Shift + M')
            speak("how can i help you sir?")

        elif 'lock' in  statement:

            press_and_release('Windows + L')
            speak("how can i help you sir?")

        elif 'switch app' in statement or 'switch' in statement:
            press_and_release('ALT + TAB')
            speak("how can i help you sir?")