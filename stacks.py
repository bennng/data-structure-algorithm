class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to store stack elements

    def push(self, item):
        self.items.append(item)  # Add the item to the top of the stack

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove and return the top item from the stack
        else:
            raise IndexError("pop from empty stack")  # Raise an error if the stack is empty

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Return the top item without removing it
        else:
            raise IndexError("peek from empty stack")  # Raise an error if the stack is empty

    def is_empty(self):
        return len(self.items) == 0  # Return True if the stack is empty, False otherwise

    def size(self):
        return len(self.items)  # Return the number of items in the stack

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())  # Output: 2
print(stack.pop())   # Output: 2
print(stack.pop())   # Output: 1
print(stack.is_empty())  # Output: True