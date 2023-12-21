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
app.geometry("380x400")
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
    )
    performCountButton.place(x=0, y=190)


renderFromTextTab(fromTextTab)


app.mainloop()
