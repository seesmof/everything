#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers, one from the beginning, one from the end
        # if the sum is smaller than the target, move the left pointer forward
        # if the sum is larger than the target, move the right pointer backward
        # if the sum is equal to the target, return the indices
        # time complexity: O(n)
        # space complexity: O(1)
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []


# @lc code=end
