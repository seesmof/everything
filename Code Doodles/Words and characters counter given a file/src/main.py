from rich import print
from rich.console import Console
from rich.table import Table
from rich.traceback import install
from rich.markdown import Markdown as md
from customtkinter import *
import threading

from components.AlertPopup import AlertPopup
from util.main import *

install()
console = Console()


app = CTk()
app.geometry("380x560")
app.resizable(False, False)
app.title("Count Words and Characters")
app.bind("<Escape>", lambda event: closeApp(app, event=event))
set_default_color_theme("dark-blue")

tabsContainer = CTkTabview(app)
tabsContainer.add("From File")
tabsContainer.add("From Text")
tabsContainer.pack(expand=True, fill="both")

fromFileTab = tabsContainer.tab("From File")
fromTextTab = tabsContainer.tab("From Text")


def renderFromFileTab(root):
    getFileNameHeading = CTkLabel(
        root,
        text="Enter name of the file to count words in",
        font=("Arial", 14, "bold"),
    )
    getFileNameHeading.place(x=0, y=0)

    getFileNameInput = CTkEntry(root, placeholder_text="Enter text here...", width=240)
    getFileNameInput.place(x=0, y=30)

    getFileNameButton = CTkButton(
        root,
        text="Perform Count",
        width=110,
        font=("Arial", 12, "bold"),
    )
    getFileNameButton.place(x=245, y=30)


renderFromFileTab(fromFileTab)


def removeWhiteSpace(data):
    lines = data.split("\n")
    lines = [line for line in lines if line != ""]
    return lines, len(lines)


def countSymbols(lines):
    res = 0
    for line in lines:
        symbolsInLine = 0
        for char in line:
            symbolsInLine += 1
        res += symbolsInLine
    return res


def countWords(lines):
    res = 0
    for line in lines:
        wordsInLine = line.split(" ")
        res += len(wordsInLine)
    return res


def getMostPopularWords(lines):
    words = {}
    for line in lines:
        wordsInLine = line.split(" ")
        for word in wordsInLine:
            if (
                word == ""
                or word == " "
                or word == "."
                or word == "!"
                or word == "?"
                or word == "("
                or word == ")"
                or word == ","
                or word == "~"
                or word == "-"
                or word == "'"
                or word == '"'
                or word == "”"
                or word == "“"
                or word == "’"
                or word == "+"
            ):
                continue

            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    return words


def renderFromTextTab(root):
    def showMostPopularWords(data):
        console.log(
            f"Started calculating most popular words from a text with {len(data)} words..."
        )

        lines, _ = removeWhiteSpace(data)
        mostPopularWords = getMostPopularWords(lines)
        mostPopularWords = sorted(
            mostPopularWords.items(), key=lambda x: x[1], reverse=True
        )

        resultsString = "Most popular words in a given text:\n"
        for word in mostPopularWords:
            resultsString += f"  - {word[0]}: {word[1]}\n"
        AlertPopup(resultsString)

        console.log(f"Calculated {len(mostPopularWords)} most popular words")

    def performCalculations(data):
        lines, linesCount = removeWhiteSpace(data)
        symbolsCount = countSymbols(lines)
        wordsCount = countWords(lines)

        resultsLines.configure(text=f"Lines: {linesCount}")
        resultsSymbols.configure(text=f"Symbols: {symbolsCount}")
        resultsWords.configure(text=f"Words: {wordsCount}")

    getTextHeading = CTkLabel(
        root, text="Enter text you want to count words in", font=("Arial", 14, "bold")
    )
    getTextHeading.place(x=0, y=0)

    getTextInput = CTkTextbox(root, width=360, height=150)
    getTextInput.place(x=0, y=30)
    getTextInput.bind(
        "<KeyRelease>",
        lambda event: performCalculations(getTextInput.get("0.0", "end")),
    )

    resultsLines = CTkLabel(root, text="", font=("Arial", 13))
    resultsLines.place(x=0, y=190)

    resultsSymbols = CTkLabel(root, text="", font=("Arial", 13))
    resultsSymbols.place(x=100, y=190)

    resultsWords = CTkLabel(root, text="", font=("Arial", 13))
    resultsWords.place(x=240, y=190)

    showMostPopularWordsButton = CTkButton(
        root,
        text="Show Most Popular Words (Might Take Some Time)",
        font=("Arial", 12, "bold"),
        command=lambda: showMostPopularWords(getTextInput.get("0.0", "end")),
        width=360,
    )
    showMostPopularWordsButton.place(x=0, y=220)


renderFromTextTab(fromTextTab)


app.mainloop()
