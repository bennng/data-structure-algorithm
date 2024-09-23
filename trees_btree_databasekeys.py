class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree (defines the range for number of keys)
        self.leaf = leaf  # True if leaf node, else False
        self.keys = []  # List of keys
        self.children = []  # List of child pointers

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode(self.t, False)
            temp.children.insert(0, self.root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, key)
            self.root = temp
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BTreeNode(t, y.leaf)
        parent.children.insert(i + 1, z)
        parent.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:(2 * t) - 1]
        y.keys = y.keys[0:t - 1]
        if not y.leaf:
            z.children = y.children[t:2 * t]
            y.children = y.children[0:t]

    def inorder(self, node):
        i = 0
        for i in range(len(node.keys)):
            if not node.leaf:
                self.inorder(node.children[i])
            print(node.keys[i], end=' ')
        if not node.leaf:
            self.inorder(node.children[i + 1])

# Example usage
btree = BTree(3)
database_keys = [10, 20, 5, 6, 12, 30, 7, 17]

for key in database_keys:
    btree.insert(key)

print("Inorder traversal of the B-Tree:")
btree.inorder(btree.root)