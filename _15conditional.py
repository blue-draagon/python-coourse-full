is_old = True
is_licenced = True

if is_old:
    print('You are old enough to drive')
elif is_licenced:
    print('You can drive !')
else:
    print('You are not old to drive')

print('checkcheck')


if is_old and is_licenced:
    print('You are ready to drive')

# in python indentation is needed to set instruction in block
# convention use 4 or multiple of 4 four indentation

# Truthy and Falsy

licence = 'A'
age = 18

if licence and age:
    print('You have licence and age')

# python automaticaly convert expression to boolean on condition test
# a truthy value is value that converted to boolean give true

# ternary operator
# value_if_condition_is_true if condition else value_if_condition_is_false
is_friend = False
can_message = 'Message allowed' if is_friend else 'Message not allowed'
print(can_message)

# short circuiting
# seconds terms of condtion if not evaluated when whatever these result
# the value of the condition do not change
if 15 or print('test1'):
    print('condtion is true')
# the second operation is not evauated

if 15 and print('test2'):
    print('condtion is true')
# it is not evaluated

if False and print('test3'):
    print('condtion is true')
else:
    print('condition is false')

# logical operator
# and
# or
# > greater than
# < less than
# == equal
# != not equal
# >= greater than or equal
# <= less than or equal
# not : the oposite
print(not True)

# operation combinasion
print(1 < 2 < 3 < 4)