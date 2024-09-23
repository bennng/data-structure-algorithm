class TreeNode:
    def __init__(self, key):
        self.key = key  # Stock price
        self.left = None  # Left child
        self.right = None  # Right child
        self.height = 1  # Height of the node

class AVLTree:
    def __init__(self):
        self.root = None  # Initialize the root of the tree to None

    def insert(self, root, key):
        if not root:
            return TreeNode(key)  # Create a new node if tree is empty

        if key < root.key:
            root.left = self.insert(root.left, key)  # Insert in the left subtree
        else:
            root.right = self.insert(root.right, key)  # Insert in the right subtree

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))  # Update the height of the node

        balance = self.get_balance(root)  # Get the balance factor

        # Perform rotations to balance the tree
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)  # Delete from the left subtree
        elif key > root.key:
            root.right = self.delete(root.right, key)  # Delete from the right subtree
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))  # Update the height of the node

        balance = self.get_balance(root)  # Get the balance factor

        # Perform rotations to balance the tree
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def get_max_value_node(self, root):
        if root is None or root.right is None:
            return root
        return self.get_max_value_node(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=' ')
            self.inorder(root.right)

# Example usage
avl = AVLTree()
root = None

# Add stock prices
stock_prices = [50, 30, 70, 20, 40, 60, 80]
for price in stock_prices:
    root = avl.insert(root, price)

# Display all stock prices in sorted order
print("Stock Prices in Sorted Order:")
avl.inorder(root)
print()

# Find the minimum and maximum stock prices
min_node = avl.get_min_value_node(root)
max_node = avl.get_max_value_node(root)
print(f"Minimum Stock Price: {min_node.key}")
print(f"Maximum Stock Price: {max_node.key}")

# Remove a stock price
root = avl.delete(root, 70)
print("\nStock Prices after Deleting 70:")
avl.inorder(root)
print()