# This program introduced a data collection: list
lst = list()

lst.append(13)
# print(lst)
lst.append(15)
lst.append(15)
lst.append(15)

lst[2] = 6
print(lst)

# lst.clear()
# print(lst)

# lst.copy()
# print(lst)

t = list()
t.append('a')
print(t)
lst.extend(t)
print(lst)

lst.insert(1, 4)
print(lst)

# lst.pop([2])
# print(lst)

lst.remove(15)
print(lst)

lst.reverse()
print(lst)
