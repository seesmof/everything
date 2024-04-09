import json
from os import path
from bs4 import BeautifulSoup
import requests
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()
currentDir: str = path.dirname(path.abspath(__file__))


def getBibleVerse(Book: str, chapter: int, verse: int, version: str = "NASB"):
    soup = getSoup(Book, chapter, verse, version)
    # find div with class "result-text" and read text from a p element inside of it, which is the only element in contains
    verseClass = f"{Book[:3]}-{chapter}-{verse}"
    verseElement = soup.find("span", attrs={"class": verseClass})

    if verseElement:
        verseText = "".join(verseElement.find_all(string=True, recursive=False))
        return verseText.strip()
    else:
        return "Verse not found"


def getSoup(Book: str, chapter: int, verse: int, version: str = "NASB"):
    url = f"https://www.biblegateway.com/passage/?search={Book}%20{chapter}%3A{verse}&version={version}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


"""
queries = ["John 3:16", "Romans 6:23", "John 4:16", "1 John 4:16"]
for query in queries:
    Book, chapterAndVerse = query.rsplit(" ", 1)
    chapter, verse = chapterAndVerse.split(":")
    content = getBibleVerse(Book, chapter, verse)
    console.print(content)
"""

Books = [
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
    "Song of Songs",
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
]


def writeBibleBooks() -> None:
    for Book in Books:
        soup = getSoup(Book, 1, 1)
        outputFile: str = path.join(currentDir, "BibleBooks", f"{Book}.txt")
        with open(outputFile, "w", encoding="utf-8") as f:
            f.write(f"{soup}")


BibleBookCorrespondances = {Book: "" for Book in Books}
BooksCorrespondancesJson: str = path.join(currentDir, "BibleBookCorrespondances.json")
with open(BooksCorrespondancesJson, "w", encoding="utf-8") as f:
    json.dump(BibleBookCorrespondances, f, indent=2)

"""
<p> <span class="text Rom-6-23" id="en-NASB-28080"><sup class="versenum">23 </sup>For the wages of <sup class="crossreference" data-cr="#cen-NASB-28080A" data-link='(&lt;a href="#cen-NASB-28080A" title="See cross-reference A"&gt;A&lt;/a&gt;)'>(<a href="#cen-NASB-28080A" title="See cross-reference A">A</a>)</sup>sin is death, but the gracious gift of God is <sup class="crossreference" data-cr="#cen-NASB-28080B" data-link='(&lt;a href="#cen-NASB-28080B" title="See cross-reference B"&gt;B&lt;/a&gt;)'>(<a href="#cen-NASB-28080B" title="See cross-reference B">B</a>)</sup>eternal life in Christ Jesus our Lord.</span></p> <a class="full-chap-link" href="/passage/?search=Romans%206&amp;version=NASB" title="View Full Chapter">Read full chapter</a>
"""
