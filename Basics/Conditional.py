# This program takes in a number and checks if equal to zero, positive or negative

num = int(input("Enter a number: "))

if num == 0:
    print("The number you entered is equal to zero")
elif num > 0:
    print("The number you entered is a positive number")
else:
    print("The number you entered is a negative number")