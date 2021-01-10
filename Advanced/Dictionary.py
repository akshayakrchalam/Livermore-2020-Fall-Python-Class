# This program is all about Dictionaries and built-in methods

dt = {"First Name": "Akshaya", "Last Name": "Krishna"}
# {key:value, key:value}
print(dt.keys())
print(dt.values())
print(dt.items())
# del dt
print(dt)

num = int(input("Enter a number: "))
dt["Number"] = num
print(dt)

num = int(input("Enter a number: "))
k = input("Enter a key: ")
dt[k] = num
print(dt)