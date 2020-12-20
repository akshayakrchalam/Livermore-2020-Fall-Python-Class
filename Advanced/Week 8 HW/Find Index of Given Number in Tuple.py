# Find the index of a given number in the tuple
lst = [1, 2, 3, 4, 5]

tup = tuple(lst)
print(tup)
num = int(input("Enter a number in the above tuple to find its index: "))
flag = False
for n in range(0, 5):
    if tup[n] == num:
        flag = True
        print("The index of the number you entered is: ", n)
        break
if flag == False:
    print("Sorry the number you entered does not exist in the tuple!")
