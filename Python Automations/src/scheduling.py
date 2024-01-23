from os import path
from time import sleep
from datetime import date
import schedule as scheduler
from rich.console import Console
from rich.traceback import install

from utils.misc import *

install()
console = Console()

currentDir = path.dirname(path.abspath(__file__))
schedulePath = path.join(currentDir, "..", "data", "schedule.json")
# schedulePath = path.join(currentDir, "..", "data", "archive", "2_1.json")
miscDataPath = path.join(currentDir, "..", "data", "misc.json")

miscData = readJson(miscDataPath)
classTimes = miscData["class_times"]

scheduleData = readJson(schedulePath)
courses, schedule = scheduleData["courses"], scheduleData["schedule"]

if date.today().isocalendar()[1] % 2 == 0:
    weekStatus = "Знаменник"
    speak("Week is Denominator.")
else:
    weekStatus = "Чисельник"
    speak("Week is Numerator.")

try:
    dayName = date.today().strftime("%A")
    scheduleClasses(
        day=dayName,
        week=weekStatus,
        schedule=schedule,
        scheduler=scheduler,
        times=classTimes,
        disciplines=courses,
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
