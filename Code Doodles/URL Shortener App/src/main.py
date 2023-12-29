"""
so what we need is
- input field where user will enter his URL
- output field next to it that will show the shortened URL
- two buttons next to it saying Shorten and Copy
- additional feature toggles below like Auto Copy and Auto Open in Browser
"""

from customtkinter import *
from rich.console import Console
from rich.traceback import install
from pyshorteners import Shortener

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

        self.grab_set()
        self.lift()
        self.bind("<Escape>", self.closePopup)

    def closePopup(self, event):
        self.destroy()


class Heading(CTkLabel):
    def __init__(self, root, text, font=("Arial", 14, "bold")):
        super().__init__(root, text=text, font=font)


class Button(CTkButton):
    def __init__(self, root, text, width=1, command=None, font=("Arial", 12, "bold")):
        super().__init__(root, text=text, command=command, width=width, font=font)


class App:
    def __init__(
        self,
        title="Python GUI",
        width=600,
        height=400,
        colorTheme="dark-blue",
    ):
        self.app = CTk()
        self.setupApp(title, width, height, colorTheme)
        self.tabsContainer = self.setupTabsContainer(self.app)

    def setupApp(self, title, width, height, colorTheme):
        self.app.geometry(f"{width}x{height}")
        self.app.title(title)
        self.app.resizable(False, False)
        set_default_color_theme(colorTheme)
        self.app.bind("<Escape>", self._closeApp)

    def setupTabsContainer(self, root):
        tabsContainer = CTkTabview(root)
        tabsContainer.pack(fill="both", expand=True)

        return tabsContainer

    def addTab(self, name):
        tab = self.tabsContainer.add(name)
        return tab

    def _closeApp(self, event):
        self.app.destroy()

    def run(self):
        self.app.mainloop()

    def shortenUrl(self):
        url = self.inputUrlBox.get()
        if url == "":
            AlertPopup("Please enter URL to shorten")
            console.log("[red]Failed to shorten URL since none was entered[/]")
        else:
            shortener = Shortener()
            shortUrl = shortener.tinyurl.short(url)
            self.resultsBox.delete(0, "end")
            self.resultsBox.insert("end", shortUrl)


def main():
    app = App(height=400, width=600, title="URL Shortener")

    mainTab = app.addTab("Shorten your URL")

    app.inputUrlBox = CTkEntry(
        mainTab,
        placeholder_text="Enter URL to shorten",
        width=200,
    )
    app.inputUrlBox.place(x=0, y=0)

    app.resultsBox = CTkEntry(
        mainTab,
        width=200,
        placeholder_text="Shortened URL here...",
    )
    app.resultsBox.place(x=205, y=0)

    app.shortenUrlButton = Button(
        mainTab, text="Shorten", width=70, command=app.shortenUrl
    )
    app.shortenUrlButton.place(x=410, y=0)

    app.copyUrlButton = Button(
        mainTab,
        text="Copy",
        command=lambda: console.copy(
            app.resultsBox.get() if app.resultsBox.get() else None
        ),
    )
    app.copyUrlButton.place(x=485, y=0)

    app.run()


if __name__ == "__main__":
    main()
