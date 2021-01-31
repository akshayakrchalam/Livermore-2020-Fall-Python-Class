# Packages and Modules - Built-in & User-Defined

# User-Defined
# Importing package and calling functions
import hello
print(hello.say_hello())
print(hello.hello_there("Python"))

# Import modules from package
from hello import hello_there
print(hello_there("Akshaya"))

# Built-in
import sys
from random import randint

var = randint(0, 100)
print("The random integer from 0 - 100 is: %d" % var)

for n in range(0, 9):
    if n > 5:
        # Doesn't print 6-8
        sys.exit()
    print(n)
# print("Python!")
