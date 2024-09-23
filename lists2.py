tanks = ['Tiger', 'Sherman', 'Panther', 'Hellcat', 'Chaffee']
tanks.append('Abrams')
print(tanks)

mixedlist = ['apple', 3, 'orange', 5, 'banana', 9.12]
print(mixedlist)
emptylist = []
print(emptylist)
anotherlist = list()
print(anotherlist)

print(tanks[0])
print(tanks[1])
print(tanks[2])

print(tanks[-1])
print(tanks[-3])
      
print(tanks[1:4])
print(tanks[1:])
print(tanks[:3])
print(tanks[:])
print(tanks[::2])
print(tanks[::-1])

tanks.append('T-34')
print(tanks)

tanks.insert(3, 'Type 59')
print(tanks)

tanks.remove('Sherman')
print(tanks)

concatenated_tanks = tanks + ['M1', 'M60', 'M48']
concatenated_mixed = tanks + mixedlist
print(concatenated_mixed)

for item in concatenated_mixed:
    print(item)

squares = [x**2 for x in range(110)]
print(squares)

for corner in squares:
    print(corner)