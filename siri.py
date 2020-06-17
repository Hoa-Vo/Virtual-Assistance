import pyttsx3
from datetime import date
import wikipedia

# pip install pipwin32
# pipwin install pyaudio
# pip install pyttsx3
# pip install wikipedia


def findWiki():
    username = input("Enter your name: ")
    text = "Hello " + username + " , input infomation you need to find, i will do it for you"
    engine.say(text)
    engine.runAndWait()
    while True:
        find = input("Input infomation: ")
        print("Robot:....")
        try:
            content = wikipedia.summary(find, sentences=1)
            print("Find it!!!")
            print(content)
            engine.say(content)
            engine.runAndWait()
        except:
            print("Can't find!!!")
            engine.say("Can't find, try another one")
            engine.runAndWait()


# main
engine = pyttsx3.init()
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
findWiki()
# today = date.today()
# engine.say(today.strftime("%d %B %Y"))
