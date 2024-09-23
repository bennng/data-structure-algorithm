def two_sum(nums, target):
    # Create an empty dictionary to store numbers and their indices
    seen = {}
    
    # Iterate over the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement (what we need to add to the current number to get the target)
        complement = target - num
        
        # Check if the complement is already in the dictionary
        if complement in seen:
            # If complement is found, return the indices of the current number and the complement
            return [seen[complement], i]
        
        # If the complement is not found, store the current number and its index in the dictionary
        seen[num] = i

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Outputs: [0, 1]