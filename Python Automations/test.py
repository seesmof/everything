import re


def isPalindrome(s: str) -> bool:
    strippedString = re.sub(r"\W+", "", s)
    strippedString = strippedString.lower()
    strippedString = strippedString.replace("_", "")
    print(strippedString)
    return strippedString == strippedString[::-1]


inputString = "ab_a"
res = isPalindrome(inputString)
print(res)
inputString = "A man, a plan, a canal: Panama"
res = isPalindrome(inputString)
print(res)
