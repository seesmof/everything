from rich import print
from rich.console import Console
from rich.table import Table
from rich.traceback import install
from rich.markdown import Markdown as md
from customtkinter import *
from collections import defaultdict
import threading

from components.AlertPopup import AlertPopup
from util.main import *

install()
console = Console()


def countLines(data):
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
    words = defaultdict(int)
    for line in lines:
        wordsInLine = line.split(" ")
        for word in wordsInLine:
            if word not in {"", " ", ".", "!", "?", "-"}:
                words[word] += 1
    return words


def showMostPopularWords(data):
    console.log(
        f"Started calculating most popular words from a text with {len(data)} words..."
    )

    lines, _ = countLines(data)
    mostPopularWords = getMostPopularWords(lines)
    mostPopularWords = sorted(
        mostPopularWords.items(), key=lambda x: x[1], reverse=True
    )

    resultsString = "Most popular words in a given text:\n"
    for word in mostPopularWords:
        resultsString += f"  - {word[0]}: {word[1]}\n"
    AlertPopup(resultsString)

    console.log(f"Calculated {len(mostPopularWords)} most popular words")


def getCurrentMetrics(text):
    lines, linesCount = countLines(text)
    symbolsCount = countSymbols(lines)
    wordsCount = countWords(lines)
    return lines, linesCount, symbolsCount, wordsCount


def updateMetrics(text, resultsLines, resultsSymbols, resultsWords):
    lines, linesCount, symbolsCount, wordsCount = getCurrentMetrics(text)

    resultsLines.configure(
        text=f"Lines: {linesCount}" if linesCount else "No lines found"
    )
    resultsSymbols.configure(
        text=f"Symbols: {symbolsCount}" if symbolsCount else "No symbols found"
    )
    resultsWords.configure(
        text=f"Words: {wordsCount}" if wordsCount else "No words found"
    )


def renderInputSection(root):
    getTextHeading = CTkLabel(
        root, text="Enter text you want to count words in", font=("Arial", 14, "bold")
    )
    getTextInput = CTkTextbox(root, width=360, height=150)

    getTextHeading.place(x=0, y=0)
    getTextInput.place(x=0, y=30)

    return getTextHeading, getTextInput


def renderMainTab(root):
    getTextHeading, getTextInput = renderInputSection(root)

    # todo show popular words as top level component with a scrollable frame

    resultsHeading = CTkLabel(root, text="Text Results", font=("Arial", 14, "bold"))
    resultsHeading.place(x=0, y=190)

    resultsLines = CTkLabel(root, text="No lines found", font=("Arial", 13))
    resultsLines.place(x=0, y=215)

    resultsSymbols = CTkLabel(root, text="No symbols found", font=("Arial", 13))
    resultsSymbols.place(x=0, y=235)

    resultsWords = CTkLabel(root, text="No words found", font=("Arial", 13))
    resultsWords.place(x=0, y=255)

    interactWithTextHeading = CTkLabel(
        root,
        text="Text Interactions",
        font=("Arial", 14, "bold"),
    )
    interactWithTextHeading.place(x=180, y=190)

    showMostPopularWordsButton = CTkButton(
        root,
        text="Show Popular Words",
        font=("Arial", 12, "bold"),
        command=lambda: showMostPopularWords(getTextInput.get("0.0", "end")),
    )
    showMostPopularWordsButton.place(x=180, y=220)

    getTextInput.bind(
        "<KeyRelease>",
        lambda event: updateMetrics(
            getTextInput.get("0.0", "end"), resultsLines, resultsSymbols, resultsWords
        ),
    )


def main():
    app = CTk()
    app.geometry("380x560")
    app.resizable(False, False)
    app.title("Count Words and Characters")
    app.bind("<Escape>", lambda event: closeApp(app, event=event))
    set_default_color_theme("dark-blue")

    tabsContainer = CTkTabview(app)
    tabsContainer.add("Analyze Text")
    tabsContainer.pack(expand=True, fill="both")

    mainTab = tabsContainer.tab("Analyze Text")

    renderMainTab(mainTab)

    app.mainloop()


if __name__ == "__main__":
    main()
