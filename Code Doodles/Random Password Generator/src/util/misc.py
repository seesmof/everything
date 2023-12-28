import json
from os import path
from rich.console import Console
from rich.traceback import install
from customtkinter import *

install()
console = Console()


def closeApp(app, event):
    app.destroy()


def loadSettingsData():
    currentDir = path.dirname(path.abspath(__file__))
    settingsPath = path.join(currentDir, "..", "..", "data", "settings_cache.json")

    try:
        with open(settingsPath, "r") as settingsFile:
            return json.load(settingsFile)
    except Exception as e:
        console.log("[red]Failed to load settings file[/red]")
        return {
            "includeLetters": True,
            "includeUppercase": True,
            "includeNumbers": True,
            "includeSymbols": True,
            "excludeDuplicates": False,
            "length": 32,
        }


def updateOutputLength(outputLength, outputLengthHeading):
    outputLengthHeading.configure(text=f"Password Length ({int(outputLength.get())})")


def loadSettings(settings):
    loadedData = loadSettingsData()
    settings["includeLetters"] = loadedData["includeLetters"]
    settings["includeUppercase"] = loadedData["includeUppercase"]
    settings["includeNumbers"] = loadedData["includeNumbers"]
    settings["includeSymbols"] = loadedData["includeSymbols"]
    settings["excludeDuplicates"] = loadedData["excludeDuplicates"]
    settings["length"] = loadedData["length"]


def setSettings(
    settings: dict,
    includeLetters: CTkCheckBox,
    includeUppercase: CTkCheckBox,
    includeNumbers: CTkCheckBox,
    includeSymbols: CTkCheckBox,
    excludeDuplicates: CTkCheckBox,
    outputLength: CTkSlider,
):
    includeLetters.select() if settings["includeLetters"] else includeLetters.deselect()
    includeUppercase.select() if settings[
        "includeUppercase"
    ] else includeUppercase.deselect()
    includeNumbers.select() if settings["includeNumbers"] else includeNumbers.deselect()
    includeSymbols.select() if settings["includeSymbols"] else includeSymbols.deselect()
    excludeDuplicates.select() if settings[
        "excludeDuplicates"
    ] else excludeDuplicates.deselect()
    outputLength.set(settings["length"])
