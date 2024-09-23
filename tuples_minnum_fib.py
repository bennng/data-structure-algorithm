def find_min_fibonacci_numbers(k):
    fibs = [1, 1]
    while fibs[-1] < k:
        fibs.append(fibs[-1] + fibs[-2])
    
    count = 0
    for fib in reversed(fibs):
        if k >= fib:
            k -= fib
            count += 1
        if k == 0:
            break
    return count

# Example usage
k1 = 7
print("Minimum Fibonacci Numbers:", find_min_fibonacci_numbers(k1))  # Output: 2

k2 = 10
print("Minimum Fibonacci Numbers:", find_min_fibonacci_numbers(k2))  # Output: 2

k3 = 19
print("Minimum Fibonacci Numbers:", find_min_fibonacci_numbers(k3))  # Output: 3