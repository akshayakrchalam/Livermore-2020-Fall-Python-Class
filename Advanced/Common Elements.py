# This program will take the common elements from 'tup_1' and 'tup_2', which will be added in 'tup_3'
lst = []

tup_1 = ()
tup_2 = ()
tup_3 = ()

# Input values for tup_1
for n in range(0, 5):
    num = int(input("Enter a number to be in 'tup_1': "))
    lst.append(num)
tup_1 = tuple(lst)
lst.clear()

# Input values for tup_2
for i in range(0, 5):
    num_1 = int(input("Enter a number to be in 'tup_2': "))
    lst.append(num_1)
tup_2 = tuple(lst)
lst.clear()

# Finding common elements for tup_3
for a in tup_1:
    for b in tup_2:
        if a == b:
            lst.append(a)
tup_3 = tuple(lst)
print("The common elements from tup_1 and tup_2 are: ", tup_3)
