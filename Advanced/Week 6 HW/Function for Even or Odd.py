# Use a function to find if a given number is even or odd


def even_odd(num):
    if num % 2 == 0:
        print("The number you entered is even.")
    else:
        print("The number you entered is odd.")


num = int(input("Enter a number: "))
even_odd(num)
