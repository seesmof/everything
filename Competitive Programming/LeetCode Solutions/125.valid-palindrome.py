#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

import re


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strippedString = re.sub(r"\W+", "", s)
        strippedString = strippedString.lower()
        strippedString = strippedString.replace("_", "")
        return strippedString == strippedString[::-1]


# @lc code=end
