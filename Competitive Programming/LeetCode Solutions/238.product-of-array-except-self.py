#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
from math import prod


class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        generalProduct = prod(nums)
        ans = []
        for index, num in enumerate(nums):
            currentProduct = generalProduct // num
            ans.append(currentProduct)
        return ans


# @lc code=end

# [0,0]
# [-1,1,0,-3,3]
