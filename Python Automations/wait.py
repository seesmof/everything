from customtkinter import *


def initialize_widgets(homeTab):
    newClassHeading = CTkLabel(
        homeTab, text="Welcome to the new class", text_color="red"
    )
    newClassInput = CTkEntry(homeTab, placeholder_text="Enter class name", width=200)

    newClassHeading.place(x=0, y=0)
    newClassInput.place(x=0, y=30)

    return newClassHeading, newClassInput
