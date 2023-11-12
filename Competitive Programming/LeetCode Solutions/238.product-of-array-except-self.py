#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        if len(nums) < 2:
            return nums
        if len(nums) == 2 and nums[0] == 0 and nums[1] == 0:
            return [0, 0]
        ans = []
        for i in range(len(nums)):
            prod = 1
            for j, num in enumerate(nums):
                if nums[j] != nums[i] and i != j:
                    prod *= num
            ans.append(prod)
        return ans


# @lc code=end

# [0,0]
# [-1,1,0,-3,3]
