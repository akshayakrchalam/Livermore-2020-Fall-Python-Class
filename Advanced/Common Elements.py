# This program will take the common elements from 'tup_1' and 'tup_2', which will be added in 'tup_3'
lst_1 = []
lst_2 = []

tup_1 = ()
tup_2 = ()

for n in range(0, 5):
    num = int(input("Enter a number to be in 'tup_1': "))
    lst_1.append(num)

tup_1 = tuple(lst_1)
# print("Printing tup_1: ", tup_1)

for i in range(0, 5):
    num_1 = int(input("Enter a number to be in 'tup_2': "))
    lst_2.append(num_1)

tup_2 = tuple(lst_2)
# print("Printing tup_2", tup_2)
