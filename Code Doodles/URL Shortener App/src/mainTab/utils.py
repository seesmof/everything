from components import AlertPopup
from rich.console import Console
from rich.traceback import install
from pyshorteners import Shortener

install()
console = Console()


def shortenUrl(inputLinkBox, outputLinkBox):
    url = inputLinkBox.get()
    if url == "":
        AlertPopup("Please enter a URL you want to shorten")
        console.log("[red]Failed to shorten URL - No input URL was entered[/red]")
    else:
        outputLinkBox.delete(0, "end")
        shortener = Shortener()
        shortUrl = shortener.tinyurl.short(url)
        outputLinkBox.insert(0, shortUrl)
