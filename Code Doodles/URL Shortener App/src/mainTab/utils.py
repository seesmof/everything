from components import AlertPopup
from rich.console import Console
from rich.traceback import install
from pyshorteners import Shortener
import webbrowser

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
