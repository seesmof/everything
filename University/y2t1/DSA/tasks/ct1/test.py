class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.children = []


class BTree:
    def __init__(self, t=3):
        self.root = BTreeNode()
        self.t = t

    def search(self, key, node=None):
        node = node or self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return True
        elif node.leaf:
            return False
        else:
            return self.search(key, node.children[i])

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(new_root, key)
        else:
            self._insert_non_full(root, key)

    def _insert_non_full(self, x, key):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(0)
            while i >= 0 and key < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = key
        else:
            while i >= 0 and key < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self._split_child(x, i)
                if key > x.keys[i]:
                    i += 1
            self._insert_non_full(x.children[i], key)

    def _split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BTreeNode(leaf=y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:]
        y.keys = y.keys[: t - 1]
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

    def delete(self, key):
        root = self.root
        self._delete(root, key)
        if len(root.keys) == 0 and not root.leaf:
            self.root = root.children[0]

    def _delete(self, x, key):
        t = self.t
        i = 0
        while i < len(x.keys) and key > x.keys[i]:
            i += 1
        if x.leaf:
            if i < len(x.keys) and key == x.keys[i]:
                x.keys.pop(i)
            else:
                print(f"Key {key} not found.")
        else:
            if i < len(x.keys) and key == x.keys[i]:
                self._delete_internal_node(x, i)
            else:
                if len(x.children[i].keys) >= t:
                    self._delete(x.children[i], key)
                else:
                    if i > 0 and len(x.children[i - 1].keys) >= t:
                        self._borrow_from_prev(x, i)
                    elif i < len(x.children) - 1 and len(x.children[i + 1].keys) >= t:
                        self._borrow_from_next(x, i)
                    else:
                        self._merge(x, i)
                        self._delete(x.children[i], key)

    def _delete_internal_node(self, x, i):
        t = self.t
        key = x.keys[i]
        if len(x.children[i].keys) >= t:
            predecessor = self._get_predecessor(x.children[i])
            x.keys[i] = predecessor
            self._delete(x.children[i], predecessor)
        elif len(x.children[i + 1].keys) >= t:
            successor = self._get_successor(x.children[i + 1])
            x.keys[i] = successor
            self._delete(x.children[i + 1], successor)
        else:
            self._merge(x, i)
            self._delete(x.children[i], key)

    def _get_predecessor(self, x):
        while not x.leaf:
            x = x.children[-1]
        return x.keys[-1]

    def _get_successor(self, x):
        while not x.leaf:
            x = x.children[0]
        return x.keys[0]

    def _borrow_from_prev(self, x, i):
        child = x.children[i]
        sibling = x.children[i - 1]
        child.keys.insert(0, x.keys[i - 1])
        x.keys[i - 1] = sibling.keys.pop()
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())

    def _borrow_from_next(self, x, i):
        child = x.children[i]
        sibling = x.children[i + 1]
        child.keys.append(x.keys[i])
        x.keys[i] = sibling.keys.pop(0)
        if not child.leaf:
            child.children.append(sibling.children.pop(0))

    def _merge(self, x, i):
        t = self.t
        child = x.children[i]
        sibling = x.children[i + 1]
        child.keys.append(x.keys[i])
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)
        x.keys.pop(i)
        x.children.pop(i + 1)


tree = BTree()
tree.insert(1)
tree.insert(3)
tree.insert(9)
tree.insert(6)
tree.insert(7)
tree.insert(5)
print(tree.search(3))
tree.delete(3)
print(tree.search(3))
