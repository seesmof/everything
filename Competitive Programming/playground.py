from typing import List
from functools import cache
from rich.console import Console
from rich.traceback import install

install()
console = Console()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def fromArray(self, arr: List[int]):
        self.head = ListNode(arr[0])
        curr = self.head
        for i in range(1, len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next

    def display(self):
        curr = self.head
        while curr:
            console.print(curr.val, end=" -> " if curr.next else "\n")
            curr = curr.next


def reverseList(head: ListNode) -> ListNode:
    pass


arr = [7, 1, 5, 3, 6, 4]
linkedList = LinkedList()
linkedList.fromArray(arr)
linkedList.display()
