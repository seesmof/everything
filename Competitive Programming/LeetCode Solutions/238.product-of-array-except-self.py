#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
from math import prod


class Solution:
    def productExceptSelf(self, arr: [int]) -> [int]:
        res = []

        for index, item in enumerate(arr):
            arrayWithoutCurrent = [arr[j] for j in range(len(arr)) if j != index]

            currentProduct = 1
            for number in arrayWithoutCurrent:
                currentProduct *= number
            res.append(currentProduct)

        return res


# @lc code=end

# [0,0]
# [-1,1,0,-3,3]
