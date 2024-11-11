# access file from another directory
with open('app/sad.txt', mode='r') as my_file:
    text = my_file.read()
    print(text)