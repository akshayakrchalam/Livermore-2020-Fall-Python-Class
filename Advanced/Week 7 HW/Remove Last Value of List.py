# Create a list from user input and remove the last value in the list.
lst = []
for n in range(0, 5):
    num = input("Enter an input: ")
    lst.append(num)

lst.pop()
print(lst)
