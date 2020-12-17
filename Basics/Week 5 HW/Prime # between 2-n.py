# Print all the prime numbers between 2 – n, given the value of n

n = int(input("Enter a number: "))

for i in range(2, n+1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)
