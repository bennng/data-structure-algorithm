from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print(stack)
for num in list(stack):
    print(num)
    if num == 3:
        print(stack.pop())
        stack.pop()
print(stack)  # Output: deque([1, 2, 4, 5])

