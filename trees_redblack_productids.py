class RedBlackNode:
    def __init__(self, key, color='red'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = RedBlackNode(0, 'black')
        self.root = self.TNULL

    def insert(self, key):
        node = RedBlackNode(key)
        node.left = self.TNULL
        node.right = self.TNULL
        node.parent = None

        if self.root == self.TNULL:
            self.root = node
            self.root.color = 'black'
            self.root.parent = None
        else:
            self._insert(self.root, node)
            self.fix_insert(node)

    def _insert(self, root, node):
        if node.key < root.key:
            if root.left == self.TNULL:
                root.left = node
                node.parent = root
            else:
                self._insert(root.left, node)
        else:
            if root.right == self.TNULL:
                root.right = node
                node.parent = root
            else:
                self._insert(root.right, node)

    def fix_insert(self, k):
        while k != self.root and k.parent.color == 'red':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.left_rotate(k.parent.parent)
        self.root.color = 'black'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder(self, node):
        if node != self.TNULL:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

# Example usage
rbt = RedBlackTree()
product_ids = [10, 20, 30, 40, 50, 25]

for product_id in product_ids:
    rbt.insert(product_id)

print("Inorder traversal of the Red-Black tree:")
rbt.inorder(rbt.root)