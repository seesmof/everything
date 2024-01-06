from typing import Optional
from Archive.testing_imports import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:
    curr = root
    while root:
        console.print(root.val)
        root = root.left


tree = TreeNode(
    1,
    TreeNode(2, TreeNode(3, TreeNode(4))),
    TreeNode(2, TreeNode(3, TreeNode(4))),
)
isSymmetric(tree)
