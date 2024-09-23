nums1 = [1, 2, 3, 1]

def contains_duplicate(nums):
    for num in nums:
        seen = {num}
        if num in set:
            return True
        else:
            seen.add(num)
    return
    


print("Contains Duplicate:", contains_duplicate(nums1))  # Output: true