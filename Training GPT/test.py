import g4f

chatLog = [
    {
        "role": "system",
        "content": "Be as brief as you possibly can unless the user asks otherwise.",
    },
]

while True:
    getInThere = input(": ")
    print()
    chatLog.append({"role": "user", "content": getInThere})
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo_16k, messages=chatLog
    )
    print(response)
    print()
    chatLog.append({"role": "assistant", "content": response})
