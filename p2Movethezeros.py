nums = [0, 1, 0, 3, 12]

def move_zeroes(nums):
    # Pointer for placing non-zero elements
    pos = 0
    
    # First pass: Move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1
    
    # Second pass: Fill the remaining positions with zeroes
    for i in range(pos, len(nums)):
        nums[i] = 0


move_zeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]