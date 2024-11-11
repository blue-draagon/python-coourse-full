# list is a array that can contains object of any type
li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2,True, 'letters']

print(type(li))

store = [
    'notebooks', 
    'iphone',
    'coputers',
    'shoes',
    'toys',
    'grapes'
]
print(store)
print(store[1])

# list is slicable
print(store[:4])

# list mutable
store[1] = 'laptop'
print(store)

# change pointer list
same_store = store
same_store[0] = 'test copy by affectation'
print(same_store)
print(store)

# to copy list use slicing
copy_store = store[:]
copy_store[0] = 'test copy by slicing'
print(copy_store)
print(store)

# maltrx : list inside a list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(matrix)
print(type(matrix))
# access sublist
print(matrix[1])
# access element
print(matrix[0][2])

# length of a list
print(len(store))

# adding element
print(store.append('basket'))
print(store)
# append update the content of list
# and return None (return nothing)

# insert element in index
store.insert(1, 'shirts')
print(store)

# append a list
store.extend(['jeans', 'glaces', 'some things'])
print(store)

# remove latest element
store.pop()
print(store)

# remove on index
pop_result = store.pop(0)
print(store)
print(pop_result)
# pop return the removed element

# remove by value
store.remove('grapes')
print(store)

# empty a list (remove all element)
print(copy_store)
copy_store.clear()
print(copy_store)

# finding element
alpha = ['a', 'b', 'c', 'd', 'e', 'd', 'c', 'f', 'd', 'g']
print(alpha.index('c'))
# index the first index with value spefied

# test element presence in list
print('laptop' in store)
print('not present' in store)

# count how much element is on list
print(alpha.count('d'))

# sort list
alpha.sort()
print(alpha)
# sorted method sort list given as argument
# sort modified list but sorted do not

# create list with range
print(range(100))
print(list(range(100)))

# join string element
separator = ' '
sentence = separator.join(['hi', 'my name', 'is', 'john'])
print(sentence)

# list unpacking
# separate list to others variables
a, b, c = [1, 2, 3]
print(a, b, c, sep='\n')

a, b, c, *other, last = [1, 2, 3, 4, 5, 6, 7 ,8 ,9, 10]
print(a, b, c, other, last, sep='\n')



