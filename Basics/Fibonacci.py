# This program prints the first 10 numbers of the Fibonacci Series
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

first = 0
second = 1
third = first + second
print("0\n1")
print(third)

for n in range(1, 8):
    first = second
    second = third
    third = first + second
    print(third)