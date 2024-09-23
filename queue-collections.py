from collections import deque

# Initialize the queue
queue = deque()

# Add elements to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

# Print the initial queue
print("Initial queue:", queue)

# Iterate through a copy of the queue
for num in list(queue):
    print(num)
    if num == 3:
        queue.popleft()

# Print the modified queue
print("Modified queue:", queue)