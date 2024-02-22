import datetime
import json
import os
import sys
from suntime import Sun, SunTimeException
from rich.console import Console
from rich.traceback import install
import pyttsx4
import ctypes
import webbrowser
import pyperclip

install()
console = Console()


def getSunset(latitude: float = 47.838800, longitude: float = 35.139567) -> str:
    timezone = datetime.datetime.now()
    sun = Sun(latitude, longitude)

    try:
        sunsetTime = sun.get_local_sunset_time(timezone)
        return sunsetTime.strftime("%H:%M")
    except SunTimeException as e:
        console.log(f"Error: {e}")


def speak(*args) -> None:
    inputText = " ".join(args)
    console.log(inputText)

    engine = pyttsx4.init()
    engine.say(inputText)
    engine.runAndWait()


def readJson(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def writeJson(path: str, data: dict | list) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def closeWindow() -> None:
    speak("Close window.")


def goodNight() -> None:
    speak("Good night.")
    ctypes.windll.user32.LockWorkStation()


def openWorkout() -> None:
    speak("Time to work out.")
    webbrowser.open(
        "obsidian://open?vault=obsidian-main-vault&file=sport%2FWorkout%20Guide"
    )


def openClass(classData: dict, disciplineName: str, classType: str) -> None:
    originalStdout = sys.stdout
    sys.stdout = open(os.devnull, "w")

    webbrowser.open(classData["class_url"])
    notesUrl = classData.get(
        "notes_url",
        "obsidian://open?vault=everything&file=University%2F%D0%A0%D0%BE%D0%B7%D0%BA%D0%BB%D0%B0%D0%B4%20%D0%B4%D0%B7%D0%B2%D1%96%D0%BD%D0%BA%D1%96%D0%B2",
    )
    webbrowser.open(notesUrl)

    sys.stdout = originalStdout

    passcode = classData.get("passcode")
    pyperclip.copy(passcode) if passcode else None

    speak(f"Opening {disciplineName} {classType}")


def scheduleClasses(
    dayName: str,
    weekStatus: str,
    schedule: dict,
    scheduler: object,
    classTimes: dict,
    courses: dict,
) -> None:
    classesToday = schedule[weekStatus].get(dayName, {})
    if not classesToday:
        speak("No classes.")
        return

    for classTime, classDescription in classesToday.items():
        scheduledTime = classTimes[classTime]
        discipline, classType = classDescription.split(" ")
        disciplineName = courses[discipline]["full_name"]
        classData = courses[discipline][classType.lower()]
        speak(f"{disciplineName} {classType} at {scheduledTime}")

        scheduler.every().day.at(scheduledTime).do(
            openClass,
            classData=classData,
            disciplineName=disciplineName,
            classType=classType,
        )
