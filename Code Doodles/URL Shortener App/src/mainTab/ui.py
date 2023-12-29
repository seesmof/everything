from components import Button, Heading

from customtkinter import *

from mainTab.utils import openLink, shortenLink


def renderShortenSection(root):
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


def renderOptionsSection(root):
    copyLinkButton = Button(root, text="Copy Link", width=80)
    openLinkButton = Button(root, text="Open Link", width=80)
    optionsInfoHeading = Heading(root, text="Options")
    autoOpenToggle = CTkSwitch(root, text="Auto Open in Browser")
    autoCopyToggle = CTkSwitch(root, text="Auto Copy Link")

    copyLinkButton.place(x=325, y=70)
    openLinkButton.place(x=410, y=70)
    optionsInfoHeading.place(x=0, y=70)
    autoOpenToggle.place(x=0, y=100)
    autoCopyToggle.place(x=0, y=130)

    return (
        copyLinkButton,
        openLinkButton,
        optionsInfoHeading,
        autoOpenToggle,
        autoCopyToggle,
    )


def renderMainTab(root):
    (
        shorteningInfoHeading,
        inputLinkEntry,
        outputLinkEntry,
        shortenButton,
    ) = renderShortenSection(root)

    (
        copyLinkButton,
        openLinkButton,
        optionsInfoHeading,
        autoOpenToggle,
        autoCopyToggle,
    ) = renderOptionsSection(root)

    optionsElements = [autoOpenToggle, autoCopyToggle]

    """
    loadOptions(*optionsElements)

    for element in optionsElements:
        element.bind("<ButtonRelease-1>", lambda event: saveOptions(*optionsElements))
    """

    shortenButton.configure(
        command=lambda: shortenLink(inputLinkEntry, outputLinkEntry, *optionsElements)
    )
    openLinkButton.configure(
        command=lambda: openLink(outputLinkEntry.get(), inputLinkEntry.get())
    )
