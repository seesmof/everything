import pyttsx4

engine = pyttsx4.init()
voices = engine.getProperty("voices")
for voice in voices:
    print(voice)
engine.setProperty("voice", voices[0].id)


def speak_text(*args):
    input_text = " ".join(args)
    print(f"\n{input_text}\n")
    engine.say(input_text)
    engine.runAndWait()


speak_text("I am speaking text with pyttsx")
