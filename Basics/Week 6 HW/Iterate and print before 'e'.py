# In a function, iterate over a given string and print only the characters that come before the letter "e"


def before_e(str):
    for n in str:
        if n == 'a' or n == 'b' or n == 'c' or n == 'd':
            print(n)


str = input("Enter a string: ")
before_e(str)
