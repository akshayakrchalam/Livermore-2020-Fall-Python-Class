# Let's handle exceptions (try except)

try:
    var = int(input("Enter a number: "))
    print(var)
    # print(x)
except ValueError:
    print("invalid value entered")
except NameError:
    print("variable is not defined")
else:
    print("Nothing went wrong")
finally:
    print("Thank you. Goodbye!")