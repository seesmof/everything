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
