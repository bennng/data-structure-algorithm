coordinates = (10, 20, 30)

for i in coordinates:
    print(i)

for coordinate in coordinates:
    print(coordinate)   

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
result = tuple1 * 2
print(result)  # Output: (1, 2, 3, 1, 2, 3)

# Membership
print(2 in tuple1)  # Output: True
print(4 in tuple1)  # Output: False

# Length
print(len(tuple1))  # Output: 3

#Packing and Unpacking
packed_tuple = 1, 2, 3
print(packed_tuple)

a, b, c = packed_tuple
print(a)
print(b)
print(c)

