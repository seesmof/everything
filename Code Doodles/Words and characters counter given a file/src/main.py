from rich import print
from rich.console import Console
from rich.table import Table
from rich.traceback import install
from rich.markdown import Markdown as md
from customtkinter import *

from components.AlertPopup import AlertPopup
from util.main import *

install()
console = Console()


app = CTk()
app.geometry("380x410")
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


def renderFromTextTab(root):
    def performCalculations(data):
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

    performCountButton = CTkButton(
        root,
        text="Perform Count",
        width=360,
        font=("Arial", 12, "bold"),
        command=lambda: performCalculations(getTextInput.get("0.0", "end")),
    )
    performCountButton.place(x=0, y=190)

    resultsHeading = CTkLabel(
        root, text="The given text contains", font=("Arial", 14, "bold")
    )
    resultsHeading.place(x=0, y=230)

    resultsLines = CTkLabel(root, text="", font=("Arial", 13))
    resultsLines.place(x=0, y=260)

    resultsSymbols = CTkLabel(root, text="", font=("Arial", 13))
    resultsSymbols.place(x=0, y=290)

    resultsWords = CTkLabel(root, text="", font=("Arial", 13))
    resultsWords.place(x=0, y=320)


renderFromTextTab(fromTextTab)


app.mainloop()
