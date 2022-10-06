
from random import shuffle

cities = ['Tiruppur', 'Coimbatore', 'San Francisco', 'Boca Raton', "Austin", "Chennai"]

print("Before Sorting:", cities)
sortedCities = sorted(cities)
print("After Sorting:", sortedCities)
shuffle(cities)
print(cities)