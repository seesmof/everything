import ctypes
import webbrowser

from utils.misc import speak


def closeWindow():
    speak("Close window.")


def goodNight():
    speak("Good night, bro.")
    ctypes.windll.user32.LockWorkStation()


def openWorkout():
    speak("Time to work out.")
    webbrowser.open(
        "obsidian://open?vault=obsidian-main-vault&file=sport%2FWorkout%20Guide"
    )
