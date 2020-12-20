# Check if all values in the given tuple are the same
lst = [4, 4, 4, 4]

tup = tuple(lst)
if tup[0] == tup[1] and tup[0] == tup[2] and tup[0] == tup[3]:
    print("All the values in the tuple below are the same.")
else:
    print("All the values in the tuple below are different.")
print(tup)
