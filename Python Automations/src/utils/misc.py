import datetime
import json
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
    speak("Good night, bro.")
    ctypes.windll.user32.LockWorkStation()


def openWorkout() -> None:
    speak("Time to work out.")
    webbrowser.open(
        "obsidian://open?vault=obsidian-main-vault&file=sport%2FWorkout%20Guide"
    )


def scheduleClasses(
    day: str,
    week: str,
    schedule: dict,
    scheduler: object,
    times: dict,
    disciplines: dict,
) -> None:
    classesToday = schedule[week].get(day, {})
    if not classesToday:
        speak("No classes.")
        return

    for time, description in classesToday.items():
        scheduledTime = times[time]
        discipline, classType = description.split(" ")
        disciplineName = disciplines[discipline]["full_name"]
        classData = disciplines[discipline][classType.lower()]
        speak(f"{disciplineName} {classType} at {scheduledTime}")

        def openClass():
            webbrowser.open(classData["class_url"])
            notesUrl = classData.get("notes_url")
            webbrowser.open(notesUrl) if notesUrl else None
            passcode = classData.get("passcode")
            pyperclip.copy(passcode) if passcode else None

        scheduler.every().day.at(scheduledTime).do(openClass)


# TODO fix this thing, its not creating different jobs but just does the latest one. oh Gosh thats a bummer
