import string


def countHomogenous(s: str) -> int:
    alphabet = {letter: [] for letter in string.ascii_lowercase}
    givenLetters = {}
    givenArray = []
    s = sorted(s)

    for _, letter in enumerate(s):
        givenArray.append(letter)

    for index, letter in enumerate(givenArray):
        if letter in givenLetters.keys():
            givenLetters[letter] += 1
        else:
            givenLetters[letter] = 1

    print(givenLetters)


s = "aabbbbccddddd"
res = countHomogenous(s)
print(res)
s = "aaabbccc"
res = countHomogenous(s)
print(res)
s = "aaa"
res = countHomogenous(s)
print(res)
