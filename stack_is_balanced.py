def is_balanced(expression):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != matching[char]:
                return False
    return len(stack) == 0

expression = "{[()]}"
print(is_balanced(expression))  # Output: True

