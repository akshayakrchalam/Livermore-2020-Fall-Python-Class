# This is our first functions program: greet

def greet(name):
    print("Good afternoon", name, "How are you doing?")

def addition(num):
    return num + 10

name = input("Enter a name: ")
greet(name)
num = int(input("Enter a number: "))
print("Your number plus 10 is", addition(num))
