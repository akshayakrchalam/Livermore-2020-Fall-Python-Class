# This program has advanced built-in methods for a set
st_1 = {1, 2, 3, 4, 5}
st_2 = {1, 2, 3, 4, 10}

print(st_1.difference(st_2))

print(st_1.intersection(st_2))

print(st_1.union(st_2))

st_1.clear()
print(st_1)

del st_2
# print(st_2)
