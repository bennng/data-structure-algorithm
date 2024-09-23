fruits  = ["apple", "orange", "banana"]
#print(fruits[0])
#print(fruits[1])
#print(fruits[2])

#for fruit in fruits:
#    print(fruit)

fruits.append("grape")
fruits.append("kiwi")
print(fruits)
#fruits = fruits * 100
print(fruits[::2])

fruits.remove("banana")
fruits[1].replace("orange", "mango")
print(fruits)

fruits.insert(1, "mango")
print(fruits)

fruits.pop()
print(fruits)

print(fruits.pop())
print(fruits)


#numbers = list(range(20))
#print(numbers)
