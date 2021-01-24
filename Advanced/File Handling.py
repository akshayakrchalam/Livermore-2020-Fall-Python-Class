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
