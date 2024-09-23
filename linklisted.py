class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next pointer to None

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list to None

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:  # If the list is empty
            self.head = new_node  # Set the new node as the head
            return
        last = self.head  # Start from the head
        while last.next:  # Traverse to the end of the list
            last = last.next
        last.next = new_node  # Set the next pointer of the last node to the new node

    def prepend(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # Set the next pointer of the new node to the current head
        self.head = new_node  # Set the new node as the head

    def delete_with_value(self, data):
        if not self.head:  # If the list is empty
            return
        if self.head.data == data:  # If the head node contains the data to be deleted
            self.head = self.head.next  # Set the head to the next node
            return
        current = self.head  # Start from the head
        while current.next and current.next.data != data:  # Traverse the list to find the node to be deleted
            current = current.next
        if current.next:  # If the node to be deleted is found
            current.next = current.next.next  # Set the next pointer of the previous node to skip the node to be deleted

    def print_list(self):
        current = self.head  # Start from the head
        while current:  # Traverse the list
            print(current.data)  # Print the data of each node
            current = current.next  # Move to the next node

    def reverse(self):
        prev = None  # Initialize the previous node to None
        current = self.head  # Start from the head
        while current:  # Traverse the list
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the next pointer of the current node
            prev = current  # Move the previous node to the current node
            current = next_node  # Move to the next node
        self.head = prev  # Set the head to the last node processed