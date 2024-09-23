nums = [2,2,1,5,6,7,8,5,6,7,8,9,11]

# def find_single_number(nums):
#     singlenum = set()
#     seen = set()

#     for num in nums:
#         if num in seen:
#             singlenum.remove(num)

#         else: 
#             seen.add(num)
#             singlenum.add(num)
#     length = len(singlenum)
#     if length > 0:
#         return singlenum
#     return 

# answer = find_single_number(nums)
# print(answer)  # Output: {1}

def single_number(nums):
    seen = set()
    for num in nums:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)
    return seen.pop()

# Example usage
nums1 = [2, 2, 1]
print("Single Number:", single_number(nums1))  # Output: 1

nums2 = [4, 1, 2, 1, 2]
print("Single Number:", single_number(nums2))  # Output: 4

nums3 = [1]
print("Single Number:", single_number(nums3))  # Output: 1