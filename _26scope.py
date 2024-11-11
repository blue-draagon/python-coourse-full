# scope - to what variables do I have access
age = 100
# age is a global scope variable
# and can be accessing any where in program
# until he is overide


def test():
    new_age = 20
# new age is function scope
# it is not avalaible outside the function


# scope rules
a = 1


def confusion():
    a = 5
    return a


print(confusion())
print(a)

# a in confusion is on only
# on the local confusion function scope

# the scope checking
# 1 - the local scope
# 2 - parent locals
# 3 - global scope
# 4 - buid in python

# parameters of functions is relative to local function scope

# using global


def confusion():
    global a
    a = 10
    return a


print(confusion())
print(a)
# not a in confusion is refering to glabal scope a
# is not recomended to lot of use global
# is better to use dependency injection
total = 0


def inc(total):
    if total % 2 == 0:
        total += 3
    else:
        total += 1

    return total


total = inc(total)
total = inc(total)
total = inc(total)
print(total)

# using nonlocal


def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner :', x)

    inner()
    print('outer : ', x)


outer()
# nonlocal refer to variable that are in the direct parent scope
# whatever global refer to the global scope

# local scoping is important to make our program
# use less memory when he is running
