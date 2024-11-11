# string element iterator
for item in 'Zero to mastery':
    print(item, end=' ')

print()
# list element iterator
for item in [1,2,3,4,5,6]:
    print(item, end=' ')

print()
# set element iterator
for item in {1,2,3,4,5,6}:
    print(item, end=' ')

print()
# tuple element iterator
for item in (1,2,3,4,5,6):
    print(item, end=' ')

print()
print(item)
# item still avalaible after the loop


# double loup ususaly use for louping inside a matrix
matrix = [
    ['a', 'b', 'c'],
    [1, 2, 3],
    [100, 11.5, 20],
]

for line in matrix:
    for item in line:
        print(item)

# louping a dictionary
user = {
    'name' : 'John',
    'age' : 85,
    'country' : 'Palestine',
}
for item in user :
    print(item)
# top is the same like
for key in user.keys() :
    print(key, user.get(key))
# iterating values
for value in user.values() :
    print(value)
# iterating items
for item in user.items() :
    print(item)
# iterating items and unpacking
for key, value in user.items() :
    print(f'key {key} has value {value}')


# louping range
for number in range(100) :
    print(number)

for _ in range(100) :
    print(_)
# _ mean no needed value in the rest of program
# only convention

# loup in reverse order
for _ in range(50, 0, -1):
    print(_)
# third parameter is the step
for _ in range(50, 0, -5):
    print(_)

# useful range
for _ in range(2):
    print(list(range(10)))


# enumate
for char in enumerate('This is my sentence'):
    print(char)
# enumate is like a dict with index and value
print(type(enumerate('Hello the word')))
# enumate is important when index is needed