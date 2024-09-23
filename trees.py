class TreeNode:
    def __init__(self, key):
        self.left = None  # Left child
        self.right = None  # Right child
        self.val = key  # Node value

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize the root of the tree to None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)  # Create the root node if tree is empty
        else:
            self._insert(self.root, key)  # Call the recursive insert function

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)  # Insert as left child
            else:
                self._insert(node.left, key)  # Recur on the left subtree
        else:
            if node.right is None:
                node.right = TreeNode(key)  # Insert as right child
            else:
                self._insert(node.right, key)  # Recur on the right subtree

    def search(self, key):
        return self._search(self.root, key)  # Call the recursive search function

    def _search(self, node, key):
        if node is None or node.val == key:
            return node  # Return the node if found or None if not found
        if key < node.val:
            return self._search(node.left, key)  # Recur on the left subtree
        return self._search(node.right, key)  # Recur on the right subtree

    def inorder(self):
        self._inorder(self.root)  # Call the recursive in-order traversal function

    def _inorder(self, node):
        if node:
            self._inorder(node.left)  # Recur on the left subtree
            print(node.val, end=' ')  # Print the node value
            self._inorder(node.right)  # Recur on the right subtree

# Example usage
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

# In-order traversal
print("In-order traversal of the BST:")
bst.inorder()  # Output: 20 30 40 50 60 70 80

# Search for a value
print("\nSearch for 40 in the BST:")
node = bst.search(40)
print("Found" if node else "Not Found")  # Output: Found

print("\nSearch for 90 in the BST:")
node = bst.search(90)
print("Found" if node else "Not Found")  # Output: Not Found