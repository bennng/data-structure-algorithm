""" Sure! Here's a LeetCode-style question that involves using sets:

### LeetCode Question: Intersection of Two Arrays

**Problem Statement:**
Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must be unique, and you may return the result in any order.

**Example 1:**
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

**Example 2:**
```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
```

**Constraints:**
- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

**Follow-up:**
- What if the given array is already sorted? How would you optimize your algorithm?
- What if `nums1`'s size is small compared to `nums2`'s size? Which algorithm is better?
- What if elements of `nums2` are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

### Solution:
You can solve this problem using sets to find the intersection efficiently.

#### Python Code:
```python """

def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    answer = list(set1 & set2)
    return answer

# Example usage
#nums1 = [1, 2, 2, 1]
#nums2 = [2, 2]
#print("Intersection:", intersection(nums1, nums2))  # Output: [2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print("Intersection:", intersection(nums1, nums2))  # Output: [9, 4]

""" 
### Explanation:
- Convert both arrays to sets to remove duplicates and allow for efficient set operations.
- Use the `&` operator to find the intersection of the two sets.
- Convert the resulting set back to a list to match the expected output format.

This problem helps practice the use of sets for efficient data operations and understanding set operations like intersection. """