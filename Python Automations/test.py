import re


def isPalindrome(s):
    strippedString = re.sub(r"\W+", "", s)
    strippedString = strippedString.lower()
    strippedString = strippedString.replace("_", "")
    print(strippedString)
    return strippedString == strippedString[::-1]


def isPalindrome(s):
    return s[::-1]


inputString = "ab_a"
res: str = isPalindrome(inputString)
print(res)
inputString = "A man, a plan, a canal: Panama"
res = isPalindrome(inputString)
print(res)
res = isPalindrome()
res = isPalindrome(inputString)
