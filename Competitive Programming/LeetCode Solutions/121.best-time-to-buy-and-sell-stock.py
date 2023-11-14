#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if prices == sorted(prices, reverse=True):
            return 0

        minValue = min(prices)
        minIndex = prices.index(minValue)
        maxValue = max(prices[minIndex:])

        return maxValue - minValue


# @lc code=end
