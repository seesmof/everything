from os import path
import random
from time import sleep
from datetime import date
import schedule as scheduler
from rich.console import Console
from rich.traceback import install
from rich.markdown import Markdown as md

from src.utils.misc import *

install()
console = Console()

currentDir = path.dirname(path.abspath(__file__))
schedulePath = path.join(currentDir, "data", "schedule.json")
miscDataPath = path.join(currentDir, "data", "misc.json")

miscData = readJson(miscDataPath)
classTimes = miscData["class_times"]

scheduleData = readJson(schedulePath)
courses, schedule = scheduleData["courses"], scheduleData["schedule"]

versesBiblePath = path.join(currentDir, "data", "Bible_verses.json")
verses = readJson(versesBiblePath)
dailyVerse = random.choice(verses)

if date.today().isocalendar()[1] % 2 == 0:
    weekStatus = "Знаменник"
else:
    weekStatus = "Чисельник"
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

"""
Glory to Jesus Christ

daily Bible verse

day name
week status
weather
sunset time
clothes calculator by algorithm

Clothes Algorithm:
weather = fetch weather
if weather <= 5: winter coat + sweater + warm pants + winter shoes
"""

dailyMessage = f"""
[bold]Слава [green underline]Ісусу Христу[/green underline][/bold]

{dailyVerse["content"]} - [bright_green italic]{dailyVerse["name"]}[/]


Сьогодні - [bold yellow]{dayNameCorrespondings[dayName]}[/]
Тиждень - [bold yellow]{weekStatus}[/]
"""

console.print(dailyMessage)

arr = [5, 7, 2, 9, 4]
console.print(arr, list(reversed(arr)), arr[::-1], list(reversed(arr)) == arr[::-1])
