from suntime import Sun, SunTimeException
import pyttsx4
import schedule
import webbrowser
import pyperclip
import datetime
from datetime import date
import time
import ctypes

engine = pyttsx4.init()


def getSunset():
    latitude = 47.838800
    longitude = 35.139567
    timezone = datetime.datetime.now()

    sun = Sun(latitude, longitude)

    try:
        sunset_time = sun.get_local_sunset_time(timezone)
        return sunset_time.strftime("%H:%M")
    except SunTimeException as e:
        print("Error:", e)


def speak(*args):
    input_text = " ".join(args)
    print(f"\n{input_text}\n")
    engine.say(input_text)
    engine.runAndWait()


def closeWindow():
    speak("Close window.")


def sleep():
    speak("Good night, bro.")
    ctypes.windll.user32.LockWorkStation()
