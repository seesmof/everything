from datetime import date
from os import path
from rich.console import Console
from rich.traceback import install
from utils.actions import closeWindow, goodNight, openWorkout
import schedule as scheduler

from utils.misc import *

install()
console = Console()

currentDir = path.dirname(path.abspath(__file__))
# schedulePath = path.join(currentDir, "..", "data", "schedule.json")
schedulePath = path.join(currentDir, "..", "data", "archive", "2_1.json")
miscDataPath = path.join(currentDir, "..", "data", "misc.json")

miscData = readJson(miscDataPath)
classTimes = miscData["class_times"]

scheduleData = readJson(schedulePath)
courses, schedule = scheduleData["courses"], scheduleData["schedule"]

console.print()
for day in schedule["Чисельник"]:
    console.print(f"[bold]{day}[/bold]")
    for time, name in schedule["Чисельник"][day].items():
        time = classTimes[time]
        console.print(f"{name} at {time}")
    console.print()

# set the week nomination status
if date.today().isocalendar()[1] % 2 == 0:
    weekStatus = "Знаменник"
    speak("Week is Denominator.")
else:
    weekStatus = "Чисельник"
    speak("Week is Numerator.")

# schedule today's classes
dayName = date.today().strftime("%A")
try:
    # scheduleClasses(dayName, weekStatus)
    pass
except:
    console.log("Failed to schedule classes")

sunsetTime = getSunset()
# schedule all the routine actions
scheduler.every().day.at(sunsetTime).do(closeWindow)
scheduler.every().day.at("20:00").do(openWorkout)
scheduler.every().day.at("21:30").do(goodNight)
