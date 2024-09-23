""" Sure! Let's dive into dictionaries in Python. Dictionaries are a powerful and flexible data structure that allow you to store and manage data using key-value pairs.

What is a Dictionary?
A dictionary is an unordered collection of items. Each item is a pair consisting of a key and a value. Dictionaries are mutable, meaning you can change their content after they are created.

Key Characteristics:
Unordered: The items in a dictionary are not stored in any particular order.
Key-Value Pairs: Each item in a dictionary is a pair consisting of a key and a value.
Mutable: You can add, remove, or modify items in a dictionary.
Keys Must Be Unique: Each key in a dictionary must be unique. Values, however, can be duplicated.
Keys Must Be Immutable: Keys can be of any immutable data type, such as strings, numbers, or tuples.
Creating a Dictionary:
You can create a dictionary using curly braces {} or the dict() function. """



student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
print(student)
print(student["name"]) 
print(student["courses"])

for key, value in student.items():
    print(f"{key}, {value}")
    

student_grades = {"Alice": 90, "Bob": 85, "Charlie": 92}

employee_ages = dict(Alice=30, Bob=25, Charlie=35)

empty_dict = {}