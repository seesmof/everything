word = "square"


def convert(word):
    vowels = ["a", "e", "i", "o", "u"]
    if word[0] not in vowels and word[1:3] == "qu":
        word = word[3:] + word[0:3] + "ay"
    return word


res = convert(word)
print(res, res == "aresquay")
