
import array as arr

i = 5
myArray = arr.array('i', [1, 2, 3, 4, 5])
secondArray = arr.array('i', [20])
print(myArray)
print(secondArray)


# arr[:: -1] reverses the given array

print("Reverse of myArray is: ", end="")
print(myArray[::-1])
print()

print("Elements of array before reversal: ")
for i in myArray:
    print(i)

print()
revArray = myArray[::-1]
print("Elements of array after reversal: ")
for i in revArray:
    print(i)

print()


# Reversing a String
myName = "Mariya"
print(myName)
print("Reverse of given name is: ", myName[::-1])
print()

#Check if a given string is a palindrome
str1 = input("Enter a string")
print("Given String is: ", str1)
print("Reverse of the given string is: ", str1[::-1])

if (str1.lower() == str1[::-1].lower()):
    print(f"{str1} is a palindrome")
else:
    print(f"{str1} is not a palindrome")

print()

for letter in str1:
    print(letter)

