import datetime
from suntime import Sun, SunTimeException
from rich.console import Console
from rich.traceback import install
import pyttsx4

install()
console = Console()


def getSunset(latitude: float = 47.838800, longitude: float = 35.139567):
    timezone = datetime.datetime.now()
    sun = Sun(latitude, longitude)

    try:
        sunsetTime = sun.get_local_sunset_time(timezone)
        return sunsetTime.strftime("%H:%M")
    except SunTimeException as e:
        console.log(f"Error: {e}")


def speak(*args):
    input_text = " ".join(args)
    console.print(input_text)

    engine = pyttsx4.init()
    engine.say(input_text)
    engine.runAndWait()
