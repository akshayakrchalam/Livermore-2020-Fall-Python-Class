# This program is a mini calculator
# Operators - +, -, *, /, %, //, **

def addition():
    return num_1 + num_2

def subtraction():
    return num_1 - num_2

def multiplication():
    return num_1 * num_2

def division():
    return num_1 / num_2

def modulus():
    return num_1 % num_2

def integer_division():
    return num_1 // num_2

def exponent():
    return num_1 ** num_2

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
print("The sum of both numbers is", addition())
print("The difference of both numbers is", subtraction())
print("The product of both numbers is", multiplication())
print("The quotient of both numbers is", division())
print("The remainder of both numbers is", modulus())
print("The integer quotient of both numbers is", integer_division())
print("The exponential value of both numbers is", exponent())
