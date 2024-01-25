#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequencies = {num: 0 for num in nums}
        for num in nums:
            frequencies[num] += 1
        frequencies = sorted(frequencies.items(), key=lambda x: x[1])
        return frequencies[0][0]


# @lc code=end
