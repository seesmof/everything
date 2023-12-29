from components import Button, Heading

from customtkinter import *


def renderShortenTab(root):
    shorteningInfoHeading = Heading(
        root=root, text="Enter the URL you want to shorten in the box below"
    )
    inputLinkEntry = CTkEntry(
        root, placeholder_text="Enter your URL here...", width=200
    )
    outputLinkEntry = CTkEntry(
        root, placeholder_text="Shortened URL here...", width=200
    )
    shortenButton = Button(root, text="Shorten", width=80)

    shorteningInfoHeading.place(x=0, y=0)
    inputLinkEntry.place(x=0, y=30)
    outputLinkEntry.place(x=205, y=30)
    shortenButton.place(x=410, y=30)

    return shorteningInfoHeading, inputLinkEntry, outputLinkEntry, shortenButton


def renderOptionsTab(root):
    return "Not Implemented", "", "", ""


def renderMainTab(root):
    (
        shorteningInfoHeading,
        inputLinkEntry,
        outputLinkEntry,
        shortenButton,
    ) = renderShortenTab(root)

    copyLinkButton, openLinkButton, autoOpenToggle, autoCopyToggle = renderOptionsTab(
        root
    )
