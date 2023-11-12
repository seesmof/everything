#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#


# @lc code=start
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        if len(nums) < 2:
            return nums

        freq = {el: 0 for el in nums}
        for num in nums:
            freq[num] += 1

        buckets = [[] for num in nums]

        for key, value in freq.items():
            buckets[value].append(key)

        print(buckets)

        ans = []
        for i in reversed(range(len(buckets))):
            if len(ans) == k:
                break

            bucket = buckets[i]
            if bucket != []:
                while bucket != []:
                    if len(ans) == k:
                        break
                    ans.append(bucket.pop())

        return ans


# @lc code=end

# [4,1,-1,2,-1,2,3]\n2
# [5,3,1,1,1,3,73,1]\n2
