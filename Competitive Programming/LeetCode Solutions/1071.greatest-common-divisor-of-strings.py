#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#


# @lc code=start
class Solution:
    def gcdOfStrings(self, one: str, two: str) -> str:
        count = 1
        while True:
            trial = one[:count]
            if trial not in one or trial not in two:
                return trial[:-1]
            else:
                count += 1


# @lc code=end
