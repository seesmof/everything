#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#


# @lc code=start
class Solution:
    def mooveToBack(self, nums, index):
        for i in range(index, len(nums) - 1):
            tmp = -29348209482390478293472894174290213987
            nums[i] = nums[i + 1]
            nums[i + 1] = tmp
        return nums

    def removeDuplicates(self, nums: [int]) -> int:
        neededSize = len(set(nums))
        met = {}
        res = 0

        for _, el in enumerate(nums):
            met[el] = 0

        for i in range(len(nums)):
            element = nums[i]

            if element == -29348209482390478293472894174290213987:
                continue
            elif met[element] > 0:
                self.mooveToBack(nums, i)
                for j in range(len(nums)):
                    if nums[j] == element:
                        self.mooveToBack(nums, j)
            else:
                met[element] += 1

        for _ in range(len(nums) - neededSize):
            nums.pop()

        res = len(nums)
        return res


# @lc code=end
