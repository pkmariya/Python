
# this is a Class demo

print("This is a demo of Python Classes")
print()

class myParentClass():
    def method1(self):
        print("Parent class method1")

    def method2(self, someString):
        print("Parent class method2 " + someString)

myObj1 = myParentClass()
myObj1.method1()
myObj1.method2("additional String")

print()
print("Class Inheritance demo")
print()

class myChildClass(myParentClass):
    def method1(self):
        myParentClass.method1(self)
        print("Child class Method1")

    def method2(self, someString):
        myObj1.method2("New String")
        print("Child class Method2 ", someString)


myObj2 = myChildClass()
myObj2.method1()
myObj2.method2("second string")
