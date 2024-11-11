# good way to manipulate file is surround with try bloc
try :
    with open('test.txt') as file:
        pass # do some thing in the file
except FileNotFoundError:
    print('The file does not exist')
except IOError:
    print('There are an IO error')