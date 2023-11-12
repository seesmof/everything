#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

import heapq


# @lc code=start
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        if len(nums) < 2:
            return nums
        print()
        freq = {el: 0 for el in nums}
        for el in nums:
            freq[el] += 1
        print(f"FREQUENCIES: {freq}")
        pairs = []
        for key, value in freq.items():
            pair = (key, -value)
            heapq.heappush(pairs, pair)
        print(f"PAIRS: {pairs}")
        ans = []
        for i in range(k):
            tmp = heapq.heappop(pairs)
            ans.append(tmp[0])
        print(f"ANS: {ans}")
        print()
        return ans


# @lc code=end
