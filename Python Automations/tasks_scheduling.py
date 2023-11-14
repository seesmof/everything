from library import *
from year2term1classes import *

current_time = datetime.datetime.now()
current_hour = current_time.hour
current_minute = current_time.minute
today = date.today()
dayName = today.strftime("%A")
current_week = datetime.date.today().isocalendar()[1]
weather = f"Outside its {get_weather()} degrees"

classOneTime = "08:30"
classTwoTime = "10:05"
classThreeTime = "11:55"
classFourTime = "13:25"
classFiveTime = "14:55"
classSixTime = "16:45"

classOneTime_early = "08:25"
classTwoTime_early = "10:00"
classThreeTime_early = "11:50"
classFourTime_early = "13:20"
classFiveTime_early = "14:50"
classSixTime_early = "16:40"

speak_text("124 UAH daily donate.")

weekNominationStatus = ""
if current_week % 2 == 0:
    weekNominationStatus = "Знаменник"
    speak_text("This week is a Denominator.")
else:
    weekNominationStatus = "Чисельник"
    speak_text("This week is a Numerator.")

if dayName == "Saturday" or dayName == "Sunday":
    speak_text("No classes today!")
else:
    speak_text("Today's classes:")

if dayName == "Monday":
    speak_text(f"{ASD} Lecture at {classThreeTime}")
    schedule.every().day.at(classThreeTime_early).do(ASD_lecture)
    if weekNominationStatus == "Чисельник":
        speak_text(f"{TY} Practice at {classFourTime}")
        schedule.every().day.at(classFourTime_early).do(TY_practice)
        speak_text(f"{SP} Lecture at {classFiveTime}")
        schedule.every().day.at(classFiveTime_early).do(SP_lecture)
    else:
        speak_text(f"{SP} Lab at {classFourTime}")
        schedule.every().day.at(classFourTime_early).do(SP_practice)
elif dayName == "Tuesday":
    speak_text(f"{WEB} Lab at {classOneTime}")
    schedule.every().day.at(classOneTime_early).do(WEB_practice)
    speak_text(f"{ASD} Lab at {classTwoTime}")
    schedule.every().day.at(classTwoTime_early).do(ASD_practice)
    speak_text(f"{OPI} Lab at {classFiveTime}")
    schedule.every().day.at(classFiveTime_early).do(OPI_practice)
    if weekNominationStatus == "Знаменник":
        speak_text(f"{OPI} Practice at {classFourTime}")
        schedule.every().day.at(classFourTime_early).do(OPI_practice)
elif dayName == "Wednesday":
    speak_text(f"{WEB} Lecture at {classTwoTime}")
    schedule.every().day.at(classTwoTime_early).do(WEB_lecture)
    if weekNominationStatus == "Чисельник":
        speak_text(f"{TY} Lecture at {classOneTime}")
        schedule.every().day.at(classOneTime_early).do(TY_lecture)
elif dayName == "Thursday":
    if weekNominationStatus == "Чисельник":
        speak_text(f"{IY} Practice at {classFiveTime}")
        schedule.every().day.at(classFiveTime_early).do(IY_practice)
    else:
        speak_text(f"{OPI} Lecture at {classTwoTime}")
        schedule.every().day.at(classTwoTime_early).do(OPI_lecture)
        speak_text(f"{IY} Lecture at {classFiveTime}")
        schedule.every().day.at(classFiveTime_early).do(IY_lecture)
elif dayName == "Friday":
    if weekNominationStatus == "Чисельник":
        speak_text(f"{VM} Lecture at {classTwoTime}")
        schedule.every().day.at(classTwoTime_early).do(VM_lecture)
        speak_text(f"{VM} Practice at {classThreeTime}")
        schedule.every().day.at(classThreeTime_early).do(VM_practice)


sunsetTime = get_sunset()
schedule.every().day.at(sunsetTime).do(close_window)

while True:
    schedule.run_pending()
    time.sleep(3)
