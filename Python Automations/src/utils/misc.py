import datetime
import json
import os
import sys
from bs4 import BeautifulSoup
import requests
from suntime import Sun, SunTimeException
from rich.console import Console
from rich.traceback import install
import pyttsx4
import ctypes
import webbrowser
import pyperclip

install()
console = Console()
openWeatherApiKey = "de0da57ef7133cd5dc35076a664291c5"


def getSunset(latitude: float = 47.838800, longitude: float = 35.139567) -> str:
    timezone = datetime.datetime.now()
    sun = Sun(latitude, longitude)

    try:
        sunsetTime = sun.get_local_sunset_time(timezone)
        return sunsetTime.strftime("%H:%M")
    except SunTimeException as e:
        console.log(f"Error: {e}")


def getWeatherScrape(city: str = "Запоріжжя") -> str:
    url = f"https://www.google.com/search?q=weather+{city}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    temperature = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
    return temperature


def getWeatherOpenWeather(city: str = "Запоріжжя") -> str:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={openWeatherApiKey}"
    response = requests.get(url)
    data = response.json()
    temperature = data["main"]["temp"]
    return temperature


def getClothing(weather: str | int) -> str:
    if type(weather) == str and "°" in weather:
        weather = weather.split("°")[0]
    weather = int(weather)

    if weather <= -5:
        return "зимова куртка + светр + теплі штани + зимове взуття"
    elif weather <= 5:
        return "зимова куртка + футболка + теплі штани + зимове взуття"
    elif weather <= 15:
        return "легка куртка + светр + теплі штани + легке взуття"
    elif weather <= 20:
        return "светр + легкі штани + легке взуття"
    else:
        return "футболка + шорти + легке взуття"


def getMonthName(month: int) -> str:
    if month == 1:
        return "Січень"
    elif month == 2:
        return "Лютий"
    elif month == 3:
        return "Березень"
    elif month == 4:
        return "Квітень"
    elif month == 5:
        return "Травень"
    elif month == 6:
        return "Червень"
    elif month == 7:
        return "Липень"
    elif month == 8:
        return "Серпень"
    elif month == 9:
        return "Вересень"
    elif month == 10:
        return "Жовтень"
    elif month == 11:
        return "Листопад"
    elif month == 12:
        return "Грудень"


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

    speak(f"{disciplineName} {classType}")


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
