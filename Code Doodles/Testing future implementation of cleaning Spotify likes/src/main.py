from os import path
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

# Declare file paths
currentDir = path.dirname(path.abspath(__file__))
lyricsFile = path.join(currentDir, "..", "data", "lyrics.md")
wordsFile = path.join(currentDir, "..", "data", "forbidden_words.json")

# Open the files and load their data
with open(wordsFile, "r", encoding="utf-8") as f:
    forbiddenWords = f.read().splitlines()
with open(lyricsFile, "r", encoding="utf-8") as f:
    lyrics = f.read()

# Check the song for purity
if any(word in lyrics for word in forbiddenWords):
    console.print("[red]The song is not clean, you should ban it[/]")
else:
    console.print("[green]The song is clean 🙏[/]")

# TODO query API to see the country of origin of the song and if its moscovian, ban it
