class TreeNode:
    def __init__(self, name, phone):
        self.name = name  # Contact name
        self.phone = phone  # Contact phone number
        self.left = None  # Left child
        self.right = None  # Right child

class ContactList:
    def __init__(self):
        self.root = None  # Initialize the root of the tree to None

    def add_contact(self, name, phone):
        if self.root is None:
            self.root = TreeNode(name, phone)  # Create the root node if tree is empty
        else:
            self._add_contact(self.root, name, phone)  # Call the recursive add function

    def _add_contact(self, node, name, phone):
        if name < node.name:
            if node.left is None:
                node.left = TreeNode(name, phone)  # Insert as left child
            else:
                self._add_contact(node.left, name, phone)  # Recur on the left subtree
        else:
            if node.right is None:
                node.right = TreeNode(name, phone)  # Insert as right child
            else:
                self._add_contact(node.right, name, phone)  # Recur on the right subtree

    def search_contact(self, name):
        return self._search_contact(self.root, name)  # Call the recursive search function

    def _search_contact(self, node, name):
        if node is None or node.name == name:
            return node  # Return the node if found or None if not found
        if name < node.name:
            return self._search_contact(node.left, name)  # Recur on the left subtree
        return self._search_contact(node.right, name)  # Recur on the right subtree

    def display_contacts(self):
        self._display_contacts(self.root)  # Call the recursive in-order traversal function

    def _display_contacts(self, node):
        if node:
            self._display_contacts(node.left)  # Recur on the left subtree
            print(f"Name: {node.name}, Phone: {node.phone}")  # Print the contact details
            self._display_contacts(node.right)  # Recur on the right subtree

# Example usage
contacts = ContactList()
contacts.add_contact("Alice", "123-456-7890")
contacts.add_contact("Bob", "234-567-8901")
contacts.add_contact("Charlie", "345-678-9012")
contacts.add_contact("Diana", "456-789-0123")
contacts.add_contact("Eve", "567-890-1234")

# Display all contacts
print("Contact List:")
contacts.display_contacts()

# Search for a contact
print("\nSearching for 'Charlie':")
contact = contacts.search_contact("Charlie")
if contact:
    print(f"Found: Name: {contact.name}, Phone: {contact.phone}")
else:
    print("Not Found")

print("\nSearching for 'Frank':")
contact = contacts.search_contact("Frank")
if contact:
    print(f"Found: Name: {contact.name}, Phone: {contact.phone}")
else:
    print("Not Found")