from customtkinter import *
from rich import print
from rich.console import Console
from rich.table import Table
from rich.traceback import install
from rich.markdown import Markdown as md

install()
console = Console()


class AlertPopup(CTkToplevel):
    def __init__(
        self, message: str = "Whoops... Something went wrong", title: str = "Alert"
    ):
        super().__init__()
        self.resizable(False, False)
        self.title(title)

        infoLabel = CTkLabel(self, text=message)
        infoLabel.pack(padx=8, pady=8, anchor="center")

        dismissButton = CTkButton(
            self,
            text="Okay",
            command=self.destroy,
            font=("Arial", 12, "bold"),
            width=60,
        )
        dismissButton.pack(padx=8, pady=8, anchor="e")

        self.bind("<Escape>", self.closePopup)

    def closePopup(self, event):
        self.destroy()


def closeApp(event):
    app.destroy()


app = CTk()
app.geometry("600x400")
app.title("Python GUI")
app.bind("<Escape>", closeApp)

rootTabsContainer = CTkTabview(app)
rootTabsContainer.pack(fill="both", expand=True)

rootTabsContainer.add("Chat")
rootTabsContainer.add("Statistics")
rootTabsContainer.add("Settings")

app.mainloop()
