from os import path
from rich.console import Console
from rich.traceback import install

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

console.print(schedule)
console.print(courses)
console.print(classTimes)

"""
given this folder structure, how to properly import functions from misc.py into scheduling.py?

- modules
    - scheduling.py
- utils
    - misc.py
"""
