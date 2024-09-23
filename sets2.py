# Sure! Sets are an unordered collection of unique elements in Python. They are useful for storing items where each item must be unique and for performing common set operations like union, intersection, and difference.

# Key Characteristics of Sets:
# Unordered: The elements in a set do not have a specific order.
# Unique Elements: A set cannot contain duplicate elements.
# Mutable: Sets are mutable, meaning you can add or remove elements after the set has been created.
# No Indexing: Since sets are unordered, they do not support indexing, slicing, or other sequence-like behavior.
# Creating Sets:
# Sets can be created using curly braces {} or the set() function.
my_set = {1,2,3,9,65,3,35,67,8,9,1}
print(my_set)  # Output: {1, 2, 3, 35, 8, 65, 67, 9}
ben_set = set([3,54,5657,7,33,2,324,56767,45,33])
print(ben_set)  # Output: {33, 2, 324, 7, 45, 54, 5657, 56767, 'f'}

empty_set = set()
print(empty_set)

my_set.add(4)
print(my_set)

my_set.add(3)
print(my_set)

sorted_set = sorted(my_set)
print(sorted_set)

my_set.remove(3)
my_set.remove(1)
my_set.remove(2)
print(my_set)
my_set.discard(65)
print(my_set)
my_set.discard(68)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {32, 12, 6, 7, 8}

union_set = set1 | set2
print(sorted(union_set))
print(sorted(union_set, reverse=True))
sorted_union_set = sorted(union_set)
sumset = set()
for num in sorted_union_set:
   for num2 in sorted_union_set:
       if (num + num2) == 10:
              sumset.add(num2)
print(sumset)      
       
# Explanation:
# Union of Sets: Combine set1 and set2 using the union operator (|).
# Sorting: Print the sorted union set in both ascending and descending order.
# Single Loop with Set: Use a single loop to iterate through the union_set.
# Needed Numbers Set: Keep track of the numbers needed to reach the target sum (10).
# Check for Pairs: For each number, check if the complement (target_sum - num) is already in the needed_numbers set.
# Add to Result Set: If a valid pair is found, add both numbers to the sumset.
# Update Needed Numbers: Add the current number to the needed_numbers set.

set1 = {1, 2, 3, 4, 5}
set2 = {32, 12, 6, 7, 8}

union_set = set1 | set2
print(sorted(union_set))
print(sorted(union_set, reverse=True))

target_sum = 10
needed_numbers = set()
sumset = set()

for num in union_set:
    if target_sum - num in needed_numbers:
        sumset.add(num)
        sumset.add(target_sum - num)
    needed_numbers.add(num)

print(sumset)