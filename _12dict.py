# dictionary
# is a data type and data structuration
# element have key and value

notes = {
    'math': 18,
    'french': 11,
    'svt': 10
}
print(notes)
print(type(notes))

# access element
print(notes['french'])

# dict value can be any thins like list
# dict key must be ummatable
# dict key must be unique : latest overide firts

# print(dict['not_exist]) return error if key bot exist
print(notes.get('english'))

# use default value if not exist
print(notes.get('hg', 10))
print(notes.get('math', 10))

# create dictionary with dict
user = dict(name='John')
print(user)
print(type(user))

# find key with in
print('math' in notes)

# dict keys
print(notes.keys())

# dict values
print(notes.values())

# dict items (key, value)
print(notes.items())

# others avalaible methods
# .clear()
# .copy()
# .pop () # remove given key and return the value
# .popitem() # randomly remove a value

# update or add new item
notes.update({'informatic': 19.5})
print(notes)
notes.update({'informatic': 20})
print(notes)
