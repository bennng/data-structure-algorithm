""" Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, (4-1)*(5-1) = 3*4 = 12. """

def max_product(nums):
    nums.sort()
    numa = (nums[-1]) - 1
    numb = (nums[-2]) - 1

    answer = numa * numb
    return answer

# Example usage
nums1 = [3, 4, 5, 2]
print("Max Product:", max_product(nums1))  # Output: 12

nums2 = [1, 5, 4, 5]
print("Max Product:", max_product(nums2))  # Output: 16

nums3 = [3, 7]
print("Max Product:", max_product(nums3))  # Output: 12