"""
so what we need is
- input field where user will enter his URL
- output field next to it that will show the shortened URL
- two buttons next to it saying Shorten and Copy
- additional feature toggles below like Auto Copy and Auto Open in Browser
"""

from customtkinter import *

from mainTab.ui import renderMainTab


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
    app = App(title="URL Shortener", width=510, height=215)

    mainTab = app.addTab("Shortener")
    renderMainTab(mainTab)

    app.run()


if __name__ == "__main__":
    main()
