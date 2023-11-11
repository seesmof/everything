#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        complements = {}
        for i, num in enumerate(nums):
            complements[num] = i
        print(complements)
        for i, num in enumerate(nums):
            diff = target - num
            if diff in complements and complements[diff] != i:
                return [complements[diff], i]


# @lc code=end
