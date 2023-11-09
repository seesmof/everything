#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def calculateLength(self, list: [ListNode]) -> int:
        tmp = list
        count = 1
        while tmp.next != None:
            tmp = tmp.next
            count += 1
        return count

    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        lengthOne, lengthTwo = self.calculateLength(list1), self.calculateLength(list2)
        nodeOne, nodeTwo = list1, list2

        while nodeTwo:
            oneValue, twoValue = nodeOne.val, nodeTwo.val
            print(oneValue, twoValue)

            if nodeOne.next:
                nodeOne = nodeOne.next
            else:
                nodeOne = nodeTwo

            if nodeTwo.next:
                nodeTwo = nodeTwo.next
            else:
                break

        return nodeOne


# @lc code=end
