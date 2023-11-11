#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

import heapq


# @lc code=start
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        frequencies = {}
        for el in nums:
            frequencies[el] = frequencies.get(el, 0) + 1
        heap = []
        for key, value in frequencies.items():
            heapq.heappush(heap, (-value, key))
        ans = []
        for _ in range(k):
            pair = heapq.heappop(heap)
            ans.append(pair[1])
        return ans


# @lc code=end
