# String Manipulations

string = "I love Python Programming!"
print(string)

#Format Operators
print("The string is: %s" %(input("Enter a string: ")))
print("The integer is: %d" %(int(input("Enter an integer: "))))
print("The float is: %f" %(float(input("Enter a float: "))))

# Format Keyword
txt = "Fruits for only {price:.3f} dollars"
print(txt.format(price = 5))

# Named Indexes
txt1 = "My name is {f_name} and I'm {age}".format(f_name = "John", age = 25)
# Numbered Indexes
txt2 = "My name is {1} and I'm {0}".format(25, "John")
# Empty Placeholders
txt3 = "My name is {} and I'm {}".format("John", 25)
print(txt1)
print(txt2)
print(txt2)

# Manipulating Strings
str1 = "Good afternoon"
str2 = "I am ready to learn"
str3 = str1 + str2
print(str3)
print(str3*3)
print("Akshaya" in str3)
print("Akshaya" not in str3)
print("Good" in str3)
print("Good" not in str3)
