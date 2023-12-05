def toGoatLatin(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    words = sentence.split()
    for i in range(len(words)):
        if words[i][0].lower() in vowels:
            words[i] += "ma"
        elif words[i][0].lower() not in vowels:
            words[i] = words[i][1:] + words[i][0] + "ma"
        for _ in range(i + 1):
            words[i] += "a"

    return " ".join(words)


sentence = "I speak Goat Latin"
res = toGoatLatin(sentence)
print(res, res == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
