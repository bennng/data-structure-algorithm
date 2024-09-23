def max_subarray(nums):
    max_sum = nums[0]  # Initialize max_sum as the first element
    current_sum = nums[0]  # Initialize current_sum as the first element

    # Loop through the rest of the elements
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)  # Choose to extend or start fresh
        if current_sum > max_sum:
            print(num)
        max_sum = max(max_sum, current_sum)  # Update the max_sum

    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))  # Output: 6

