import os

file_path = "/projects/test.txt"

file = open(file_path, 'w')
file.write("This is the first line in the file\n")
file.close()

file = open(file_path, 'r')
for each in file:
    print(each)

file = open(file_path, 'a')
file.write("This is the second line in the file\n")
file.write("This is the third line in the file")
file.close()

os.mkdir("/projects/Files")

file_path2 = "/projects/Files/test2.txt"

file = open(file_path2, 'w')
file.write("This is the first line in file handling\n")
file.close()

file = open(file_path2, 'a')
file.write("File Handling is powerful\n")
file.write("That is why I like Python Programming\n")
file.close()

file = open(file_path2, 'r')
for each in file:
    print(each)
file.close()