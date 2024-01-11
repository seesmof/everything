import ctypes

from utils.misc import speak


def closeWindow():
    speak("Close window.")


def goodNight():
    speak("Good night, bro.")
    ctypes.windll.user32.LockWorkStation()
