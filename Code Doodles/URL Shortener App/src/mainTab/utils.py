from os import path
from components import AlertPopup
from rich.console import Console
from rich.traceback import install
from pyshorteners import Shortener
import webbrowser
import json

install()
console = Console()


def shortenLink(inputLinkBox, outputLinkBox, autoCopyToggle, autoOpenToggle):
    url = inputLinkBox.get()
    if url == "":
        AlertPopup("Please enter a URL you want to shorten")
        console.log("[red]Failed to shorten URL - No input URL was entered[/red]")
    else:
        outputLinkBox.delete(0, "end")
        shortener = Shortener()
        shortUrl = shortener.tinyurl.short(url)
        outputLinkBox.insert(0, shortUrl)

        doAutoCopy, doAutoOpen = (
            autoCopyToggle.get(),
            autoOpenToggle.get(),
        )

        if doAutoCopy:
            copyLink(outputLinkBox)

        if doAutoOpen:
            openLink(shortUrl, url)


def openLink(shortLink, fallbackLink):
    if shortLink != "":
        webbrowser.open(shortLink)
    elif fallbackLink != "":
        webbrowser.open(fallbackLink)
    else:
        AlertPopup("Please enter a URL you want to open")
        console.log("[red]Failed to open URL - No input URL was entered[/red]")


def copyLink(box):
    box.clipboard_clear()
    box.clipboard_append(box.get())


def getOptionsData():
    currentDir = path.dirname(path.abspath(__file__))
    dataFilePath = f"{currentDir}\..\..\data\settings_cache.json"

    try:
        with open(dataFilePath, "r") as f:
            data = json.load(f)
            return data
    except Exception:
        AlertPopup("Failed to load options data")
        console.log("[red]Failed to load options data[/red]")
        return {"autoOpen": False, "autoCopy": False}


def loadOptions(autoOpenToggle, autoCopyToggle):
    data = getOptionsData()

    autoOpenToggle.select() if data["autoOpen"] else autoOpenToggle.deselect()
    autoCopyToggle.select() if data["autoCopy"] else autoCopyToggle.deselect()


def saveOptions(autoOpenToggle, autoCopyToggle):
    data = getOptionsData()

    data["autoOpen"] = autoOpenToggle.get()
    data["autoCopy"] = autoCopyToggle.get()

    currentDir = path.dirname(path.abspath(__file__))
    dataFilePath = f"{currentDir}\..\..\data\settings_cache.json"

    try:
        with open(dataFilePath, "w") as f:
            json.dump(data, f)
    except Exception:
        AlertPopup("Failed to save options data")
        console.log("[red]Failed to save options data[/red]")
