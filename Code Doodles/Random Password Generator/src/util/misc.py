from util.settings import saveSettings


def closeApp(app, event):
    app.destroy()


def updatePasswordLength(outputLength, outputLengthHeading):
    outputLengthHeading.configure(text=f"Password Length ({int(outputLength.get())})")


def bindSettingChangeEvent(widget, settings, settingsElements):
    widget.bind(
        "<ButtonRelease-1>", lambda event: saveSettings(settings, *settingsElements)
    )
