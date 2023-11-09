#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#


# @lc code=start
class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        res = digits[:]
        res[-1] += 1
        el = res[-1]
        if el // 10 != 0:
            digit = el % 10
            high = el // 10
            res[-1] = high
            res.append(digit)
        return res


# @lc code=end
