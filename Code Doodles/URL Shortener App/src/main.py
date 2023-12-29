"""
so what we need is
- input field where user will enter his URL
- output field next to it that will show the shortened URL
- two buttons next to it saying Shorten and Copy
- additional feature toggles below like Auto Copy and Auto Open in Browser
"""

from customtkinter import *


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


def main():
    app = App(height=400, width=600, title="URL Shortener")

    mainTab = app.addTab("Shorten your URL")

    heading = Heading(mainTab, text="Shorten your URL")
    heading.pack(pady=8)

    button = Button(mainTab, text="Shorten")
    button.pack(pady=8)

    app.run()


if __name__ == "__main__":
    main()
