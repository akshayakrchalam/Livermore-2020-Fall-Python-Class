# Iterate over a given input(string), and print all the vowels

str = input("Enter a string: ")

for n in str:
    if n == "a" or n == "e" or n == "i" or n == "o" or n == "u":
        print(n)