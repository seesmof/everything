def _deleteInternalNode(self, parent, index):
    # Get the minimum degree of the B-tree
    t = self.t

    # Get the key of the parent node at the given index
    key = parent.keys[index]

    # Check if the left child of the parent has enough keys to borrow from
    if len(parent.children[index].keys) >= t:
        # Get the predecessor key from the left child
        predecessor = self._getPredecessor(parent.children[index])

        # Replace the key at the given index with the predecessor key
        parent.keys[index] = predecessor

        # Recursively delete the predecessor key from the left child
        self._delete(parent.children[index], predecessor)

    # Check if the right child of the parent has enough keys to borrow from
    elif len(parent.children[index + 1].keys) >= t:
        # Get the successor key from the right child
        successor = self._getSuccessor(parent.children[index + 1])

        # Replace the key at the given index with the successor key
        parent.keys[index] = successor

        # Recursively delete the successor key from the right child
        self._delete(parent.children[index + 1], successor)

    # If both the left and right children don't have enough keys to borrow from
    else:
        # Merge the child at the given index with its right sibling
        self._merge(parent, index)

        # Recursively delete the key from the merged child
        self._delete(parent.children[index], key)
