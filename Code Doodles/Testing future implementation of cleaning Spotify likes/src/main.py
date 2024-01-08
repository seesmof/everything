from os import path
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()
curseWords = [
    "bitch",
    "fuck",
    "cunt",
    "nigga",
    "nigger",
    "whore",
    "dick",
    "pussy",
    "shit",
    "asshole",
]

currentDir = path.dirname(path.abspath(__file__))
lyricsFile = path.join(currentDir, "..", "data", "lyrics.md")
with open(lyricsFile, "r", encoding="utf-8") as f:
    lyrics = f.read()

if any(word in lyrics for word in curseWords):
    console.print("[red]The song is not clean, you should ban it[/]")
else:
    console.print("[green]The song is clean 🙏[/]")

# TODO query API to see the country of origin of the song and if its moscovian, ban it
