#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

from collections import *


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        table = {"".join(sorted(el)): [] for el in strs}
        print(table)
        for el in strs:
            ss = "".join(sorted(el))
            if ss in table:
                table[ss].append(el)
        return list(table.values())


# @lc code=end
