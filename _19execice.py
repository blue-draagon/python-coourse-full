# counter
my_list = [1,2,3,4,5,6,7,8,9,10]

the_sum = 0
for item in my_list:
    the_sum += item

print('the sum of element is :', the_sum)

# print the index
for index, value in enumerate(list(range(100, 1000))):
    if value == 500:
        print('the index of 500 is', index)