
from unicodedata import name


print("====== Lists & Tuples ========\n")

myList = [1, "One", 1.2, True, 1, 1.2, ['a', 'b', 'c'], 10]
myTuple = (1, "One", 1.3, True, 1, 10, 1.3)

# *** ways to convert a list into a tuple  ****
# myTuple = list(map(tuple, myList))
# myTuple = [tuple(l) for l in myList]

print("Sample List  is: ", myList)
print("Sample Tuple is: ", myTuple)
print()


print("***** Iterating thru List *****")
for lisVal in myList:
    print(lisVal)

print()

print("***** Iterating thru Tuple ******")
for tupVal in myTuple:
    print(tupVal)

print()

myList.append("New Value")
myList.append(10)


print("List after adding new elements: ", myList)

print("Count of 1.3 in my Tuple is: ", myTuple.count(1.3))
print("Size of my tuple is: ", myTuple.__sizeof__())
print()

print("*** Converting a real number to a Complex number ***")
realNum = 10.5
comNum = complex(realNum)
print("Complex number is: ", comNum)
print()

print("*** convert a char into an Integer")
myChar = "M"
print("Integer of myChar is: ", ord(myChar))

print()

print(" ***** init or constructor function in python ******")
# Python __init__() method is automatically called to allocate memory when an object instance of a class is created

class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

E1 = Employee("Mariya", 50, 500000)
print(E1.name, E1.age, E1.salary)
print()

print("*** Lambda Function ****")

a = lambda x, y : x+y
print("Lambda addition: ", a(10, 20))
print()

