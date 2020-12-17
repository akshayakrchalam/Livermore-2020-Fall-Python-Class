# Using the same list, replace the word “Python” with the 3rd value
lst = []
for n in range(0, 5):
    num = input("Enter an input: ")
    lst.append(num)

lst.pop()
print(lst)
lst[2] = "Python"
print(lst)