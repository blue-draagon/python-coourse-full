# function
def say_hello():
    print('Hellooooo')

say_hello()

# function is use to store multiples actions
# and call whatever we want
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]
def print_tree():
    for line in picture:
        for pixel in line:
            if not pixel :
                print(' ', end='')
            else:
                print('*', end='')
        print()

print_tree()
print_tree()

# location on memery
print(print_tree)

# arguments & parameters
# parameters is on function definition
# arguments is on function calling

# new definition overide last function
# there name and emoji are parameters
def say_hello(name, emoji):
    print(f'Hellooooo {name} {emoji}')

# there john and emoji are arguments
say_hello('John' , '😇')
say_hello('Toto' , '😇')
say_hello('Arno' , '😇')

# positional argument
# argument must be called in the order there are defined
say_hello('😇' , 'Demba')

# or in unorder with keyword arguments
say_hello(emoji='😇' , name='Samba')


# kerword arguments can be confused with
# default arguments
def say_hello(name='Fatima', emoji='😍'):
    print(name, emoji)

# default arguements function can be called without arguments
say_hello()
say_hello('Sidi')
say_hello('Modou', '😇')
print(say_hello())
# function return no if there are not return value

# the return value
def double(number=1):
    return 2 * number

print(double(10))

# funcion sould do one thing really well
# or function sould calcul or get and retur something

# function inside function
def calcul(num1, num2):
    def subcalcul(value):
        return value ** 2
    return num2 + subcalcul(num1)


print(calcul(5, 10))

# no code is executed after a return

# there are difference between methods and functions

# function docstrings
def test(a):
    '''
    Info : this function print his parameter
    '''
    print(a)

test('!!!!')
# help(test)
print(test.__doc__)


# clean code
# 4
def is_odd_or_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False
    
print(is_odd_or_even(15))
# 3 most clean
def is_odd_or_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_odd_or_even(10))
# 2 most clean
def is_odd_or_even(num):
    if num % 2 == 0:
        return True
    return False

print(is_odd_or_even(1))
# 1 most clean : better code
def is_odd_or_even(num):
    return num % 2 == 0

print(is_odd_or_even(1))

# *args and **kwargs
def super_func(*notes, **infos):
    print(notes)
    print(infos)
    for key, value in infos.items():
        print(key, value, sep=' : ')
    mean  = sum(notes) / len(notes)
    print('mean notes :', mean)

super_func(17,20,13,14,12.5,name='Modou', subject='Math')


# order of parameter
# 1 : simple params
# 2 : *args params
# 3 : default params
# 4 : **kwargs params
