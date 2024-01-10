from suntime import Sun, SunTimeException
import pyttsx4
import schedule
import webbrowser
import pyperclip
import datetime
from datetime import date
import time
import ctypes
import os
from rich.console import Console
from rich.traceback import install

install()
console = Console()


engine = pyttsx4.init()

classTimes = {
    "1": "08:30",
    "2": "10:05",
    "3": "11:55",
    "4": "13:25",
    "5": "14:55",
    "6": "16:45",
}


def getSunset(latitude: float = 47.838800, longitude: float = 35.139567):
    timezone = datetime.datetime.now()
    sun = Sun(latitude, longitude)

    try:
        sunsetTime = sun.get_local_sunset_time(timezone)
        return sunsetTime.strftime("%H:%M")
    except SunTimeException as e:
        console.log(f"Error: {e}")


def speak(*args):
    input_text = " ".join(args)
    console.print(input_text)
    engine.say(input_text)
    engine.runAndWait()


def closeWindow():
    speak("Close window.")


def sleep():
    speak("Good night, bro.")
    ctypes.windll.user32.LockWorkStation()
