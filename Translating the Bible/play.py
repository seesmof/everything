Bible_Books = {
    "Old Testament": [
        "Genesis",
        "Exodus",
        "Leviticus",
        "Numbers",
        "Deuteronomy",
        "Joshua",
        "Judges",
        "Ruth",
        "1 Samuel",
        "2 Samuel",
        "1 Kings",
        "2 Kings",
        "1 Chronicles",
        "2 Chronicles",
        "Ezra",
        "Nehemiah",
        "Esther",
        "Job",
        "Psalms",
        "Proverbs",
        "Ecclesiastes",
        "Song of Solomon",
        "Isaiah",
        "Jeremiah",
        "Lamentations",
        "Ezekiel",
        "Daniel",
        "Hosea",
        "Joel",
        "Amos",
        "Obadiah",
        "Jonah",
        "Micah",
        "Nahum",
        "Habakkuk",
        "Zephaniah",
        "Haggai",
        "Zechariah",
        "Malachi",
    ],
    "New Testament": [
        "Matthew",
        "Mark",
        "Luke",
        "John",
        "Acts",
        "Romans",
        "1 Corinthians",
        "2 Corinthians",
        "Galatians",
        "Ephesians",
        "Philippians",
        "Colossians",
        "1 Thessalonians",
        "2 Thessalonians",
        "1 Timothy",
        "2 Timothy",
        "Titus",
        "Philemon",
        "Hebrews",
        "James",
        "1 Peter",
        "2 Peter",
        "1 John",
        "2 John",
        "3 John",
        "Jude",
        "Revelation",
    ],
}

from os import path
import os
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

console.print(
    f"Books in the Old Testament: {len(Bible_Books['Old Testament'])} and Books in the New Testament: {len(Bible_Books['New Testament'])}.\n{len(Bible_Books['Old Testament']) + len(Bible_Books['New Testament'])} total Books."
)
currentDir: str = path.dirname(path.abspath(__file__))
currentTranslation: str = path.join(currentDir, "AMP to UKR")
OT_Folder = path.join(currentTranslation, "Old Testament")
NT_Folder = path.join(currentTranslation, "New Testament")

# create folder for each book in both New and Old Testament folders
for book in Bible_Books["Old Testament"]:
    os.makedirs(path.join(OT_Folder, book), exist_ok=True)
for book in Bible_Books["New Testament"]:
    os.makedirs(path.join(NT_Folder, book), exist_ok=True)
