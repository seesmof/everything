with open("input.txt", encoding="utf-8") as f:
    text = f.read()

characters = sorted(list(set(text)))
vocabularySize = len(characters)
print(f"{vocabularySize} unique characters: {''.join(characters)}")

stringToInteger = {character: index for index, character in enumerate(characters)}
integerToString = {index: character for index, character in enumerate(characters)}
encode = lambda string: [stringToInteger[character] for character in string]
decode = lambda integerList: "".join([integerToString[index] for index in integerList])

print(encode(text))
print(decode(encode(text)))
