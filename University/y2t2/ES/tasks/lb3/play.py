import requests
from rich.console import Console
from rich.traceback import install

install()
console = Console()

baseUrl = "https://bible-api.com/"


def getRandomVerse():
    request = requests.get(baseUrl + "?random=verse")
    return request.json()


translations = [
    "asv",
    "bbe",
    "darby",
    "dra",
    "kjv",
    "web",
    "webbe",
]


def getAllTranslations():
    for t in translations:
        request = requests.get(baseUrl + "Isaiah 12:2" + "?translation=" + t)
        verseText = request.json()["text"]
        console.print(t.upper() + ": " + verseText)


def printTranslationsUpper():
    for t in translations:
        console.print(t.upper())


printTranslationsUpper()

translationsUpper = [
    "ASV",
    "BBE",
    "DARBY",
    "DRA",
    "KJV",
    "WEB",
    "WEBBE",
]
