def closeApp(app, event):
    app.destroy()


def updateOutputLength(outputLength, outputLengthHeading):
    outputLengthHeading.configure(text=f"Password Length ({int(outputLength.get())})")
