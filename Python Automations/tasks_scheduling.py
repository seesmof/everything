from library import *
from year2term1classes import *

classOneTime = "08:30"
classTwoTime = "10:05"
classThreeTime = "11:55"
classFourTime = "13:25"
classFiveTime = "14:55"
classSixTime = "16:45"

classTimes = {
    "Чисельник": {
        "Monday": {
            classThreeTime: "DSA Lecture",
            classFourTime: "TY Practice",
            classFiveTime: "SP Lecture",
        },
        "Tuesday": {
            classOneTime: "WEB Practice",
            classTwoTime: "DSA Practice",
            classFiveTime: "OPI Practice",
        },
        "Wednesday": {
            classOneTime: "TY Lecture",
            classTwoTime: "WEB Lecture",
        },
        "Thursday": {
            classFiveTime: "IY Practice",
        },
        "Friday": {
            classTwoTime: "VM Lecture",
            classThreeTime: "VM Practice",
        },
    },
    "Знаменник": {
        "Monday": {
            classThreeTime: "DSA Lecture",
            classFourTime: "SP Practice",
        },
        "Tuesday": {
            classOneTime: "WEB Practice",
            classTwoTime: "DSA Practice",
            classFourTime: "OPI Practice",
            classFiveTime: "OPI Practice",
        },
        "Wednesday": {
            classTwoTime: "WEB Lecture",
        },
        "Thursday": {
            classTwoTime: "OPI Lecture",
            classFiveTime: "IY Lecture",
        },
    },
}


def scheduleClasses(day, week):
    classes = classTimes[week].get(day, {})
    if not classes:
        speak("No classes.")
        return

    for time, description in classes.items():
        discipline, type = description.split(" ")
        fullName = disciplineNames.get(discipline, discipline)
        speak(f"{fullName} {type} at {time}")

        funcName = f"{discipline}_{type.lower()}"
        func = globals().get(funcName)

        hour, minute = map(int, time.split(":"))
        minute -= 5
        time = f"{hour:02d}:{minute:02d}"

        schedule.every().day.at(time).do(func)


weekNominationStatus = ""
if datetime.date.today().isocalendar()[1] % 2 == 0:
    weekNominationStatus = "Знаменник"
    speak("Week is Denominator.")
else:
    weekNominationStatus = "Чисельник"
    speak("Week is Numerator.")

dayName = date.today().strftime("%A")
scheduleClasses(dayName, weekNominationStatus)

sunsetTime = getSunset()
schedule.every().day.at(sunsetTime).do(closeWindow)
schedule.every().day.at("21:30").do(sleep)

while True:
    schedule.run_pending()
    time.sleep(3)
