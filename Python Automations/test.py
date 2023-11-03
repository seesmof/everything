class Node:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:
    def __init__(self, t):
        self.root = Node(True)
        self.t = t

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = Node()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        if x.leaf:
            x.keys.append((k, None))
            x.keys.sort(key=lambda x: x[0])
        else:
            i = 0
            while i < len(x.keys) and k > x.keys[i][0]:
                i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i][0]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = Node(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t : (2 * t) - 1]
        y.keys = y.keys[0 : t - 1]
        if not y.leaf:
            z.child = y.child[t : 2 * t]
            y.child = y.child[0 : t - 1]


####


# Define Node class that will serve as the base structure for BTree Node
class Node:
    # Initialize node, with optional parameter to specify if node is a leaf node or not
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []

        self.leaf = leaf  # Leaf status (True for leaf, False otherwise)
        self.keys = []  # List of keys
        self.child = []  # List of child nodes


# Define B-Tree (Balanced Tree) class
class BTree:
    # Initialize tree with root as a leaf node and t as tree degree
    def __init__(self, t):
        self.root = Node(True)
        self.t = t

    # Function to Insert node
    def insert(self, k):
        root = self.root
        # Check if root node is full
        if len(root.keys) == (2 * self.t) - 1:
            temp = Node()
            self.root = temp
            temp.child.insert(0, root)
            temp = Node()  # Create temporary node
            self.root = temp  # Reassign root
            temp.child.insert(0, root)  # Insert old root as child of new root
            # Split child
            self.split_child(temp, 0)
            # Call non-full insert function
            self.insert_non_full(temp, k)
        else:
            # If root is not full, start inserting into it
            self.insert_non_full(root, k)

    # Function to insert nonfull node
    def insert_non_full(self, x, k):
        # If node is leaf, insert key into the keys list
        if x.leaf:
            x.keys.append((k, None))
            # Ensure keys are sorted
            x.keys.sort(key=lambda x: x[0])
        else:
            i = 0
            # Find child node position that will hold new key
            while i < len(x.keys) and k > x.keys[i][0]:
                i += 1
            # If found child is full
            if len(x.child[i].keys) == (2 * self.t) - 1:
                # Split the child
                self.split_child(x, i)
                # Determine which of the two children to descend to
                if k > x.keys[i][0]:
                    i += 1
            # Recursive call to the right child
            self.insert_non_full(x.child[i], k)

    # Function to split child node
    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = Node(y.leaf)
        y = x.child[i]  # child node
        z = Node(y.leaf)  # new child node after split

        # Insert new child's key and child
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])

        # Assign keys and child nodes to newly created node
        z.keys = y.keys[t : (2 * t) - 1]
        y.keys = y.keys[0 : t - 1]

        # If node is internal node, assign child nodes to child nodes of newly created node
        if not y.leaf:
            z.child = y.child[t : 2 * t]
            y.child = y.child[0 : t - 1]
