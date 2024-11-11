# list , set , dictionary


# list

my_list = []
for char in 'Helloooooooooooo':
    my_list.append(char)

print(my_list)


# can be done with
my_list = [char for char in 'Hiiiiiiiiii']
print(my_list)


my_list = [num for num in range(100)]
print(my_list)


my_list = [num ** 2 for num in range(100)]
print(my_list)


my_list = [num ** 2 for num in range(100) if num % 2 == 0]
print(my_list)

# set is working similary like list
print()

# dict

keys = [num for num in range(10)]
values = [num ** 2 for num in range(10)]
my_dict = dict(zip(keys, values))

new_dict = {key: value + 1 for key, value in my_dict.items()}
print(new_dict)

new_dict_even = {
    key: value for key, value in my_dict.items() if value % 2 == 0
}
print(new_dict_even)

print()

my_dict = {num: num * 2 for num in [1, 2, 3, 4]}
print(my_dict)
