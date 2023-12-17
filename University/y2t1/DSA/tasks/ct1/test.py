def _splitChild(self, parent, index):
    # Get the degree of our tree for convenience
    t = self.t

    # Get the child node to be split
    child = parent.children[index]

    # Create a new node for the child
    newNode = BTreeNode(leaf=child.leaf)

    # Insert the new node into the parent node
    parent.children.insert(index + 1, newNode)

    # Insert the middle key of the child node into the parent node
    parent.keys.insert(index, child.keys[t - 1])

    # Split the child node's keys
    newNode.keys = child.keys[t:]
    child.keys = child.keys[: t - 1]

    # If the child node is not a leaf, split its children nodes as well
    if not child.leaf:
        newNode.children = child.children[t:]
        child.children = child.children[:t]
