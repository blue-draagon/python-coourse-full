# lambda expressions
from functools import reduce
my_list = [1, 2, 3, 4, 1, 4, 5, 7]
print(list(map(lambda item: 2*item, my_list)))
print(my_list)

# lambda is a single expression function

print(reduce(lambda acc, item: acc + item, my_list))
