# safe way to open and close file
with open('test.txt') as my_file:
    print(my_file.readlines())


# opening mode
with open('test.txt', mode='r+') as my_file:
    text = my_file.write('Write some content')
    print(text)

# r+ mode write at index and override existing text
# a append mode print to end of text
# w clean content and write

# creating a file
# to create file use w mode
with open('new.txt', mode='w') as my_file:
    text = my_file.write(':(')
    print(text)

