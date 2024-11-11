# while loup
# infinite loup until condition
i = 0
while i < 1:
    i += 1
    print(i)
    if i == 100:
        print('We are going to break')
        break
else:
    print('The condition is not satisfied on ', i)

# condition must be false to stop the loup
# keyword break can be use to stop the loup

# else is execute if there are not break

# louping like for
my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

# usualy usage of while
while True:
    print('Enter quit to exit')
    name = input('Your name : ')
    print('Your name is', name)
    if name == 'quit':
        print('You have quit')
        break

 # break also is avalaible on for loup
 # continue keyword
for item in my_list:
    if item == 2:
        continue
    print(item)


for item in my_list:
    # do some thing here later
    pass
