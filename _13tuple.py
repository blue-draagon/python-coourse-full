# a tuple is an unmutable list
my_tuple = (1,2, 5,3,4,5)

print(my_tuple)
print(type(my_tuple))
# access element
print(my_tuple[0])
# slicing
print(my_tuple[0:3])

# test presence
print(4 in my_tuple)

# dictionary items return a list of tuple
# tuple can be use as dict key

# almost manupulation avalaible for list is
# also avalaible for tuple

# tuple unpacking return list variables
a, b, c, *others = my_tuple
print(a, b, c, others, sep='\n')

# tupe have only two methods
# .count
print(my_tuple.count(3))
# .index
print(my_tuple.index(4))
print(sorted(my_tuple))