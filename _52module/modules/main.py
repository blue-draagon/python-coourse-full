# # use module import is a better practice
# # never use import *
# # import all from module is a bad practice
#
# from utility import divide, multiply
# from shopping import shopping_cart
#
# print(shopping_cart.buy('Quran'))
# print(divide(5, 4))
# print(multiply(5, 4))
#
#
# # __main__
# print(__name__)
#
# # the running file as __main__ as package name


import random

# print((random))
# help(random)
# print(dir(random))
print(random.random()) # random number between 0 and 1
print(random.randint(20, 22)) # random integer between start and end
print(random.choice(range(20))) # choice single element from iterator
no_order = list(range(50))
random.shuffle(no_order)
print(no_order)
