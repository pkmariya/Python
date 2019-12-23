myName = "Mariya Caroline"
mySpouseName = "Preeths"

# Simple function (no arguments)
def display():
    print("hello ", myName, mySpouseName, "!")

display()

# Function with Arguments
def display(num1, num2):
    print("Addition of given numbers is: ", num1+num2)

display(10, 15)


# Function with default argument

def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

print(power(2))
print(power(2, 3))
print(power(x=3, num=5))    #named arguments in any order is accepted in python



