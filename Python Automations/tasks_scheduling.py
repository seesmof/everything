from library import *
from classes_year_2_term_2 import *
from rich import print
from rich.console import Console
from rich.traceback import install
from rich.markdown import Markdown as md

install()
console = Console()


def scheduleClasses(day, week):
    classes = currentSchedule[week].get(day, {})
    if not classes:
        speak("No classes.")
        return

    for time, description in classes.items():
        discipline, type = description.split(" ")
        speak(f"{disciplineNames[discipline]} {type} at {time}")

        hour, minute = map(int, time.split(":"))
        time = f"{hour:02d}:{minute-5:02d}"
        func = globals().get(f"{discipline}_{type.lower()}")

        schedule.every().day.at(time).do(func)


weekNominationStatus = ""
if datetime.date.today().isocalendar()[1] % 2 == 0:
    weekNominationStatus = "Знаменник"
    speak("Week is Denominator.")
else:
    weekNominationStatus = "Чисельник"
    speak("Week is Numerator.")

dayName = date.today().strftime("%A")
try:
    scheduleClasses(dayName, weekNominationStatus)
except:
    console.log("Failed to schedule classes")

sunsetTime = getSunset()
schedule.every().day.at(sunsetTime).do(closeWindow)
schedule.every().day.at("21:30").do(sleep)

while True:
    schedule.run_pending()
    time.sleep(3)
