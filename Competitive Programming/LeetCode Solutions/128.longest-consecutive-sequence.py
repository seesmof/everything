#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) < 2:
            return 1
        nums = sorted(nums)

        for _ in range(len(nums)):
            r = list(range(min(nums), max(nums) + 1))
            if set(r).issubset(set(nums)):
                return len(r)
            else:
                nums = nums[:-1]

        return 0


# @lc code=end
