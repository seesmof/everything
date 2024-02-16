from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getLen(head):
            res = 0
            while head:
                res += 1
                head = head.next
            return res

        length = getLen(head)
        mid = length // 2
        indexer = 0
        dummy = ListNode(0, head)
        cur = dummy

        while cur:
            if indexer == mid:
                cur.next = cur.next.next if cur.next else None

            indexer += 1
            cur = cur.next
        return dummy.next
