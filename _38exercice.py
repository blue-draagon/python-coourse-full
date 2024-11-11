my_list = [1, 2, 3, 4, 1, 4, 5, 7]

# square
print(list(map(lambda item: item * item, my_list)))


# List Sorting
a_list = [(0, 2), (4, 3), (9, 9), (10, -1)]
a_list.sort(key=lambda x: x[1])
print(a_list)
