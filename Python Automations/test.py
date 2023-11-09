import string


def isValid(s: str) -> bool:
    stack = []
    correspondings = {"{": "}", "(": ")", "[": "]"}

    for letter in s:
        if letter in correspondings:
            stack.append(letter)
        elif len(stack) == 0 or letter != correspondings[stack.pop()]:
            return False

    return len(stack) == 0


s = "[(){()}]({[()](){}})"
res = isValid(s)
print(res)
s = "(]"
res = isValid(s)
print(res)
