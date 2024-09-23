queue = []
# Enqueue
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeue
#first = queue.pop(0)  # Removes 1
print(queue)          # [2, 3]

for num in queue:
    print(num)
    queue.pop(0)
print(queue) 