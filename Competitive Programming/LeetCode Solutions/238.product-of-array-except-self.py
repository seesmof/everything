#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
from math import prod


class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        ans = []
        for index, num in enumerate(nums):
            exceptSelfArray = []
            for i, n in enumerate(nums):
                if i != index:
                    exceptSelfArray.append(n)
            sum = prod(exceptSelfArray)
            ans.append(sum)
        return ans


# @lc code=end

# [0,0]
# [-1,1,0,-3,3]
