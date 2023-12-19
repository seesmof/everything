from rich import print
from rich.console import Console
from rich.table import Table
from rich.traceback import install
from rich.markdown import Markdown as md
from customtkinter import *

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
        infoLabel.pack(padx=6, pady=3)

        dismissButton = CTkButton(
            self,
            text="Okay",
            command=self.destroy,
            text_color="#fff",
            fg_color="#5A4FCF",
            hover_color="#3F33BD",
            font=("Arial", 12, "bold"),
        )
        dismissButton.pack(padx=6, pady=3)

        self.bind("<Escape>", self.closePopup)

    def closePopup(self, event):
        self.destroy()


def closeApp(event):
    app.destroy()


app = CTk()
app.geometry("600x400")
app.title("Python GUI")
app.resizable(False, False)
app.bind("<Escape>", closeApp)

appColorTheme = {
    "primary": "#5A4FCF",
    "primaryHover": "#3F33BD",
}

AlertPopup()

app.mainloop()
