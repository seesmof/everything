from os import path
import random
from time import sleep
from datetime import date
import schedule as scheduler
from rich.console import Console
from rich.traceback import install
from rich.markdown import Markdown as md

from utils.misc import *

install()
console = Console()

currentDir = path.dirname(path.abspath(__file__))
schedulePath = path.join(currentDir, "..", "data", "schedule.json")
miscDataPath = path.join(currentDir, "..", "data", "misc.json")

miscData = readJson(miscDataPath)
classTimes = miscData["class_times"]

scheduleData = readJson(schedulePath)
courses, schedule = scheduleData["courses"], scheduleData["schedule"]

versesBiblePath = path.join(currentDir, "..", "data", "Bible_verses.json")
verses = readJson(versesBiblePath)
dailyVerse = random.choice(verses)

dayName = date.today().strftime("%A")
dayNameCorrespondings = {
    "Monday": "Понеділок",
    "Tuesday": "Вівторок",
    "Wednesday": "Середа",
    "Thursday": "Четвер",
    "Friday": "П'ятниця",
    "Saturday": "Субота",
    "Sunday": "Неділя",
}

with console.status("Getting weather...", spinner="point"):
    currentWeather = getWeatherScrape()
if "хуртовин" in currentWeather:
    currentWeather = currentWeather.split("\n")[-1]
clothing = getClothing(weather=currentWeather)
currentMonth = getMonthName(month=date.today().month)

if date.today().isocalendar()[1] % 2 == 0:
    weekStatus = "Знаменник"
else:
    weekStatus = "Чисельник"

dailyMessage = f"""
### Слава Ісусу Христу

> {dailyVerse["content"]} - {dailyVerse["name"]}

- Сьогодні - **{dayNameCorrespondings[dayName]}, {date.today().strftime("%d.%m.%Y")}**
- Тиждень - **{weekStatus}**
- На вулиці - **{currentWeather}**
- Одяг на вулицю - **{clothing}**
- Захід сонця - **{getSunset()}**
"""

console.print()
console.print(md(dailyMessage))
console.print()
webbrowser.open(dailyVerse["url"])

try:
    scheduleClasses(
        dayName=dayName,
        weekStatus=weekStatus,
        schedule=schedule,
        scheduler=scheduler,
        classTimes=classTimes,
        courses=courses,
    )
except:
    console.log("[red]Failed to schedule classes[/red]")

sunsetTime = getSunset()
scheduler.every().day.at(sunsetTime).do(closeWindow)
scheduler.every().day.at("20:00").do(openWorkout)
scheduler.every().day.at("21:30").do(goodNight)

while True:
    scheduler.run_pending()
    sleep(3)
