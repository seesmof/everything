#
# @lc app=leetcode id=1759 lang=python3
#
# [1759] Count Number of Homogenous Substrings
#

import string


# @lc code=start
class Solution:
    def countHomogenous(self, s: str) -> int:
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

        res = givenLetters


# @lc code=end

# FAIL
