def _borrow_from_prev(self, x, i):
    # Get the child node and its left sibling
    child = x.children[i]
    sibling = x.children[i - 1]

    # Move the key from the parent node to the child node
    child.keys.insert(0, x.keys[i - 1])

    # Move the key from the left sibling to the parent node
    x.keys[i - 1] = sibling.keys.pop()

    # If the child node is not a leaf node, move the child node's rightmost child from the left sibling
    if not child.leaf:
        child.children.insert(0, sibling.children.pop())
