from util.settings import saveSettings


def closeApp(app, event):
    app.destroy()


def updatePasswordLength(passwordLengthSlider, passwordLengthHeading):
    passwordLengthHeading.configure(
        text=f"Password Length ({int(passwordLengthSlider.get())})"
    )


def bindSettingChangeEvent(widget, settings, settingsElements):
    widget.bind(
        "<ButtonRelease-1>", lambda event: saveSettings(settings, *settingsElements)
    )
