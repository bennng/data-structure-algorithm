class Node:
    def __init__(self, data):
        self.data = data  # Store the webpage data (URL)
        self.prev = None  # Initialize the previous pointer to None
        self.next = None  # Initialize the next pointer to None

class BrowserHistory:
    def __init__(self):
        self.head = None  # Initialize the head of the history to None
        self.tail = None  # Initialize the tail of the history to None
        self.current = None  # Initialize the current pointer to None

    def visit(self, url):
        new_node = Node(url)  # Create a new node with the URL
        if not self.head:  # If the history is empty
            self.head = self.tail = self.current = new_node  # Set the new node as the head, tail, and current
        else:
            self.current.next = new_node  # Set the next pointer of the current node to the new node
            new_node.prev = self.current  # Set the previous pointer of the new node to the current node
            self.tail = self.current = new_node  # Update the tail and current to the new node

    def back(self):
        if self.current and self.current.prev:  # If there is a previous page
            self.current = self.current.prev  # Move the current pointer to the previous node
            print(f"Moved back to: {self.current.data}")
        else:
            print("No previous page.")

    def forward(self):
        if self.current and self.current.next:  # If there is a next page
            self.current = self.current.next  # Move the current pointer to the next node
            print(f"Moved forward to: {self.current.data}")
        else:
            print("No next page.")

    def display_current_page(self):
        if self.current:  # If there is a current page
            print(f"Current page: {self.current.data}")
        else:
            print("No current page.")

    def display_history(self):
        current = self.head  # Start from the head
        if not current:
            print("History is empty.")
            return
        print("Browser History:")
        while current:  # Traverse the history
            print(current.data)  # Print the URL of each node
            current = current.next  # Move to the next node

# Example usage
history = BrowserHistory()

# Visit webpages
history.visit("https://example.com")
history.visit("https://example.com/about")
history.visit("https://example.com/contact")

# Display the current page
print("Current page:")
history.display_current_page()

# Move back in history
print("\nMoving back:")
history.back()
history.display_current_page()

# Move forward in history
print("\nMoving forward:")
history.forward()
history.display_current_page()

# Display the entire history
print("\nBrowser history:")
history.display_history()