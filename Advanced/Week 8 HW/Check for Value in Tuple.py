# Check whether a given value exists in a tuple
lst = [1, 2, 3, 4, 5]

tup = tuple(lst)
num = int(input("Enter a number to check if it exists in a tuple: "))

flag = False
for n in range(0, 5):
    if tup[n] == num:
        flag = True

if flag == True:
    print("The number you entered exists in the tuple below:")
else:
    print("The number you entered does not exist in the tuple below: ")
print(tup)

# Below is another way to do the exercise
# if num in tup:
#   print("The number you entered exists in the tuple below: ")
# else:
#   print("The number you entered does not exist in the tuple below: ")
# print(tup)