from customtkinter import *

from util.misc import updateOutputLength
from util.settings import loadSettings, saveSettings, setSettings


def renderGenerateSection(root):
    generatePasswordHeading = CTkLabel(
        root,
        text="Generated password will be placed in the box below",
        font=("Arial", 14, "bold"),
    )
    passwordOuput = CTkEntry(
        state="disabled",
        master=root,
        width=250,
    )
    generatePassword = CTkButton(
        root, width=80, text="Generate", font=("Arial", 12, "bold")
    )
    copyPassword = CTkButton(root, width=60, text="Copy", font=("Arial", 12, "bold"))

    generatePasswordHeading.place(x=0, y=0)
    passwordOuput.place(x=0, y=30)
    generatePassword.place(x=255, y=30)
    copyPassword.place(x=340, y=30)

    return generatePasswordHeading, passwordOuput, generatePassword, copyPassword


def renderSettingsSection(root):
    changeSettingsHeading = CTkLabel(
        root,
        text="Change Generation Settings",
        font=("Arial", 14, "bold"),
    )
    toggleLetters = CTkCheckBox(
        root, text="Include letters", font=("Arial", 12, "bold")
    )
    toggleUppercaseLetters = CTkCheckBox(
        root, text="Include uppercase letters", font=("Arial", 12, "bold")
    )
    toggleNumbers = CTkCheckBox(
        root, text="Include numbers", font=("Arial", 12, "bold")
    )
    toggleSpecialCharacters = CTkCheckBox(
        root, text="Include special characters", font=("Arial", 12, "bold")
    )
    excludeDuplicateCharacters = CTkCheckBox(
        root, text="Exclude duplicate characters", font=("Arial", 12, "bold")
    )
    outputLengthHeading = CTkLabel(
        root, text="Password Length", font=("Arial", 12, "bold")
    )
    outputLength = CTkSlider(root, from_=8, to=64, number_of_steps=56, width=400)

    changeSettingsHeading.place(x=0, y=70)
    toggleLetters.place(x=0, y=100)
    toggleUppercaseLetters.place(x=0, y=130)
    toggleNumbers.place(x=0, y=160)
    toggleSpecialCharacters.place(x=0, y=190)
    excludeDuplicateCharacters.place(x=0, y=220)
    outputLengthHeading.place(x=0, y=250)
    outputLength.place(x=0, y=280)

    return (
        changeSettingsHeading,
        toggleLetters,
        toggleUppercaseLetters,
        toggleNumbers,
        toggleSpecialCharacters,
        excludeDuplicateCharacters,
        outputLengthHeading,
        outputLength,
    )


def renderMainTab(root):
    (
        generatePasswordHeading,
        passwordOuput,
        generatePassword,
        copyPassword,
    ) = renderGenerateSection(root)

    (
        changeSettingsHeading,
        toggleLetters,
        toggleUppercaseLetters,
        toggleNumbers,
        toggleSpecialCharacters,
        excludeDuplicateCharacters,
        outputLengthHeading,
        outputLength,
    ) = renderSettingsSection(root)

    outputLength.bind(
        "<B1-Motion>",
        lambda event: updateOutputLength(outputLength, outputLengthHeading),
    )

    localSettings = {
        "includeLetters": True,
        "includeUppercase": True,
        "includeNumbers": True,
        "includeSymbols": True,
        "excludeDuplicates": True,
        "length": 32,
    }

    loadSettings(localSettings)
    setSettings(
        localSettings,
        toggleLetters,
        toggleUppercaseLetters,
        toggleNumbers,
        toggleSpecialCharacters,
        excludeDuplicateCharacters,
        outputLength,
    )
    updateOutputLength(outputLength, outputLengthHeading)

    toggleLetters.bind(
        "<Button-1>",
        lambda event: saveSettings(
            localSettings,
            toggleLetters,
            toggleUppercaseLetters,
            toggleNumbers,
            toggleSpecialCharacters,
            excludeDuplicateCharacters,
            outputLength,
        ),
    )
    toggleUppercaseLetters.bind(
        "<Button-1>",
        lambda event: saveSettings(
            localSettings,
            toggleLetters,
            toggleUppercaseLetters,
            toggleNumbers,
            toggleSpecialCharacters,
            excludeDuplicateCharacters,
            outputLength,
        ),
    )
    toggleNumbers.bind(
        "<Button-1>",
        lambda event: saveSettings(
            localSettings,
            toggleLetters,
            toggleUppercaseLetters,
            toggleNumbers,
            toggleSpecialCharacters,
            excludeDuplicateCharacters,
            outputLength,
        ),
    )
    toggleSpecialCharacters.bind(
        "<Button-1>",
        lambda event: saveSettings(
            localSettings,
            toggleLetters,
            toggleUppercaseLetters,
            toggleNumbers,
            toggleSpecialCharacters,
            excludeDuplicateCharacters,
            outputLength,
        ),
    )
    excludeDuplicateCharacters.bind(
        "<Button-1>",
        lambda event: saveSettings(
            localSettings,
            toggleLetters,
            toggleUppercaseLetters,
            toggleNumbers,
            toggleSpecialCharacters,
            excludeDuplicateCharacters,
            outputLength,
        ),
    )
    outputLength.bind(
        "<ButtonRelease-1>",
        lambda event: saveSettings(
            localSettings,
            toggleLetters,
            toggleUppercaseLetters,
            toggleNumbers,
            toggleSpecialCharacters,
            excludeDuplicateCharacters,
            outputLength,
        ),
    )
