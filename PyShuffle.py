
from random import shuffle

cities = ['Tiruppur', 'Coimbatore', 'San Francisco', 'Boca Raton', "Austin", "Chennai"]

print("Before Sorting:", cities)
sortedCities = sorted(cities)
print("After Sorting:", sortedCities)
shuffle(cities)
print("Just shuflle the strings", cities)


myList = [3, 2, 10, 3, 1, 1, 5, 7]

print(myList)

# .pop removes all the occurrence of given element
myList.pop(3)

# .remove removes only the first occurrence of given element
myList.remove(1)

print(myList)