my_file = open('test.txt')
print(my_file)
# read the file content
print(my_file.read())
print(my_file.read())
print(my_file.read())
# moving the reader cursor
my_file.seek(0)
print(my_file.read())

# read a single line
my_file.seek(0)
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
# read all lines as list
my_file.seek(0)
print(my_file.readlines())


# opened file must be always closed to
# the memory free and make others program can
# access it

# closing file
my_file.close()
