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

class TextEditor:
    def __init__(self):
        self.text = ""  # Initialize the text as an empty string
        self.undo_stack = Stack()  # Initialize the undo stack

    def add_text(self, new_text):
        self.undo_stack.push(self.text)  # Save the current state to the undo stack
        self.text += new_text  # Add the new text to the current text

    def undo(self):
        if not self.undo_stack.is_empty():
            self.text = self.undo_stack.pop()  # Revert to the last saved state
        else:
            print("Nothing to undo.")

    def display_text(self):
        print(f"Current text: {self.text}")

# Example usage
editor = TextEditor()

# Add text to the editor
editor.add_text("Hello, ")
editor.add_text("world!")
editor.display_text()  # Output: Current text: Hello, world!

# Undo the last action
editor.undo()
editor.display_text()  # Output: Current text: Hello, 

# Undo the last action
editor.undo()
editor.display_text()  # Output: Current text: 

# Try to undo when there's nothing to undo
editor.undo()  # Output: Nothing to undo.