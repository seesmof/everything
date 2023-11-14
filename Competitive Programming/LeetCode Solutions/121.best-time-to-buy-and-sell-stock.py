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

        minValue, minIndex = min(prices), prices.index

        return


# @lc code=end
