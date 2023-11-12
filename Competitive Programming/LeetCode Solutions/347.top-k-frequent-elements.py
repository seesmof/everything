#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

import heapq


# @lc code=start
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        freq = {el: 0 for el in nums}
        pairs = []
        ans = []

        for num in nums:
            freq[num] += 1
        for key, value in freq.items():
            pair = (-value, key)
            heapq.heappush(pairs, pair)
        for _ in range(k):
            ans.append(heapq.heappop(pairs)[1])
        return ans


# @lc code=end

# [4,1,-1,2,-1,2,3]\n2
# [5,3,1,1,1,3,73,1]\n2
