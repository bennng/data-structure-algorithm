class TreeNode:
    def __init__(self, key):
        self.left = None  # Left child
        self.right = None  # Right child
        self.val = key  # Node value

class Organization:
    def __init__(self):
        self.root = None  # Initialize the root of the tree to None

    def add_employee(self, key):
        if self.root is None:
            self.root = TreeNode(key)  # Create the root node if tree is empty
        else:
            self._add_employee(self.root, key)  # Call the recursive add function

    def _add_employee(self, node, key):
        if node.left is None:
            node.left = TreeNode(key)  # Add as left child if left is empty
        elif node.right is None:
            node.right = TreeNode(key)  # Add as right child if right is empty
        else:
            # If both left and right are occupied, add to the left subtree
            self._add_employee(node.left, key)

    def find_employee(self, key):
        return self._find_employee(self.root, key)  # Call the recursive find function

    def _find_employee(self, node, key):
        if node is None or node.val == key:
            return node  # Return the node if found or None if not found
        left_result = self._find_employee(node.left, key)  # Recur on the left subtree
        if left_result:
            return left_result
        return self._find_employee(node.right, key)  # Recur on the right subtree

    def display_structure(self):
        self._display_structure(self.root, 0)  # Call the recursive display function

    def _display_structure(self, node, level):
        if node:
            print(' ' * level * 4 + str(node.val))  # Print the node value with indentation
            self._display_structure(node.left, level + 1)  # Recur on the left subtree
            self._display_structure(node.right, level + 1)  # Recur on the right subtree

# Example usage
org = Organization()
org.add_employee("CEO")
org.add_employee("CTO")
org.add_employee("CFO")
org.add_employee("VP of Engineering")
org.add_employee("VP of Finance")

# Display the organization structure
print("Organization Structure:")
org.display_structure()

# Find an employee
print("\nFinding 'CFO':")
employee = org.find_employee("CFO")
print("Found" if employee else "Not Found")

print("\nFinding 'COO':")
employee = org.find_employee("COO")
print("Found" if employee else "Not Found")