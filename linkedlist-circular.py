class Node:
    def __init__(self, data):
        self.data = data  # Store the task data
        self.next = None  # Initialize the next pointer to None

class RoundRobinScheduler:
    def __init__(self):
        self.head = None  # Initialize the head of the scheduler to None
        self.tail = None  # Initialize the tail of the scheduler to None
        self.current = None  # Initialize the current pointer to None

    def add_task(self, task):
        new_node = Node(task)  # Create a new node with the task data
        if not self.head:  # If the scheduler is empty
            self.head = self.tail = new_node  # Set the new node as the head and tail
            new_node.next = self.head  # Point the next of the new node to itself (circular)
        else:
            self.tail.next = new_node  # Set the next pointer of the tail to the new node
            self.tail = new_node  # Update the tail to the new node
            self.tail.next = self.head  # Point the next of the new tail to the head (circular)

    def remove_task(self, task):
        if not self.head:  # If the scheduler is empty
            print("Scheduler is empty.")
            return
        current = self.head
        prev = self.tail
        while True:
            if current.data == task:  # If the task is found
                if current == self.head:  # If the task is at the head
                    self.head = self.head.next  # Update the head to the next node
                    self.tail.next = self.head  # Update the tail's next pointer to the new head
                elif current == self.tail:  # If the task is at the tail
                    self.tail = prev  # Update the tail to the previous node
                    self.tail.next = self.head  # Update the tail's next pointer to the head
                else:  # If the task is in the middle
                    prev.next = current.next  # Update the previous node's next pointer to skip the current node
                if current == self.head and current == self.tail:  # If the list becomes empty
                    self.head = self.tail = None
                return
            prev = current
            current = current.next
            if current == self.head:  # If we have traversed the entire list
                break
        print("Task not found in the scheduler.")

    def execute_next_task(self):
        if not self.head:  # If the scheduler is empty
            print("Scheduler is empty.")
            return
        if not self.current:  # If no task has been executed yet
            self.current = self.head  # Start with the head
        print(f"Executing task: {self.current.data}")
        self.current = self.current.next  # Move to the next task

    def display_tasks(self):
        if not self.head:  # If the scheduler is empty
            print("Scheduler is empty.")
            return
        current = self.head
        print("Tasks in the scheduler:")
        while True:
            print(current.data)
            current = current.next
            if current == self.head:  # If we have traversed the entire list
                break

# Example usage
scheduler = RoundRobinScheduler()

# Add tasks to the scheduler
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")

# Display the tasks in the scheduler
print("Initial tasks:")
scheduler.display_tasks()

# Execute the next task
print("\nExecuting tasks:")
scheduler.execute_next_task()
scheduler.execute_next_task()
scheduler.execute_next_task()
scheduler.execute_next_task()

# Remove a task from the scheduler
print("\nRemoving Task 2:")
scheduler.remove_task("Task 2")

# Display the tasks after removal
print("\nTasks after removal:")
scheduler.display_tasks()

# Execute the next task after removal
print("\nExecuting tasks after removal:")
scheduler.execute_next_task()
scheduler.execute_next_task()