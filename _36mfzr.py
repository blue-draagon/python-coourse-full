# map filter zip reduce
# the iterator manipulator
from functools import reduce


my_list = [1, 2, 3, 4, 1, 4, 5, 7]
your_list = ['a', 'z', 'y', 'b', 'c', 'g', 'l']


def double(item):
    return 2 * item


def is_odd(item) -> bool:
    return item % 2 != 0


def compter(cpt, item):
    return cpt + item


# map
print(list(map(double, my_list)))
print(my_list)
# map execute action in all item of iterator

# filter
print(list(filter(is_odd, my_list)))
print(my_list)
# filter remove item of iterator that do not
# succes to the test function


# zip
print(list(zip(my_list, your_list)))
print(my_list)
print(your_list)
# zip groupe element of list to list of tuple
# with one element of each list
# if list len are different : the less len

# reduce
print(reduce(compter, my_list, 0))
print(my_list)
# reduce make calculation on store the result on an accumulator
