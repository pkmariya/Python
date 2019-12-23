
# loops in python

x = 0

print("While loop demo:")
# while loop
while(x<5):
    print(x)
    x = x+1

print("For loop demo:")
# for loop
y = 5
for x in range(y):
    print(x)

print("For loop in a given range:")
for x in range(5, 10):
    print(x)

print("For loop of days:")
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri","Sat"]
for d in days:
    print(d)

print("For loop printing index count and value:")
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri","Sat"]
for i, d in enumerate(days):
    print(i, d)
