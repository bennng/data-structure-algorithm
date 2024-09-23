from queue import Queue

q = Queue()

q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

for i in range(q.qsize()):
    print(q.get())
    print(q.qsize())
print(q.qsize())  # Output: 0
