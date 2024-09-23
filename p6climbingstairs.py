def climb_stairs(n):
    # Base cases
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Initialize first two steps
    first = 1
    second = 2

    # Iterate from step 3 to n
    for i in range(3, n + 1):
        current = first + second
        first = second
        second = current

    return second

n = 5
print(climb_stairs(n))  # Output: 2




