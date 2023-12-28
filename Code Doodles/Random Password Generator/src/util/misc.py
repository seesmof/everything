from string import ascii_letters, ascii_uppercase, digits
from components.AlertPopup import AlertPopup
from util.settings import saveSettings

from rich.console import Console
from rich.traceback import install
from customtkinter import *
import random

install()
console = Console()


def closeApp(app, event):
    app.destroy()


def updatePasswordLength(passwordLengthSlider, passwordLengthHeading):
    passwordLengthHeading.configure(
        text=f"Password Length ({int(passwordLengthSlider.get())})"
    )


def bindSettingChangeEvent(widget, settings, settingsElements):
    widget.bind(
        "<ButtonRelease-1>", lambda event: saveSettings(settings, *settingsElements)
    )


def copyGeneratedPassword(box):
    box.clipboard_clear()
    box.clipboard_append(box.get())


def generatePassword(box: CTkEntry, *settingsElements):
    box.delete(0, "end")

    password = ""
    useLetters = settingsElements[0].get()
    useUppercase = settingsElements[1].get()
    useNumber = settingsElements[2].get()
    useSymbols = settingsElements[3].get()
    autoCopy = settingsElements[4].get()
    length = int(settingsElements[5].get())

    if not useLetters and not useUppercase and not useNumber and not useSymbols:
        AlertPopup("Please select at least one type of character to include.")
        console.log(
            "[red]Failed to generate password: No types of characters were selected[/red]"
        )
        return

    characters = ""
    if useLetters:
        characters += ascii_letters.lower()
    if useUppercase:
        characters += ascii_uppercase
    if useNumber:
        characters += digits
    if useSymbols:
        characters += "!@#$%^&*()_+-=[]{}|;':\",./<>?`~"

    password = "".join(random.choices(characters, k=length))

    box.insert(0, password)

    if autoCopy:
        copyGeneratedPassword(box)
