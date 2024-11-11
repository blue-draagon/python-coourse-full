import sys
from random import randint

start = int(sys.argv[1])
end = int(sys.argv[2])

number = randint(start, end)

while True:
    choice = int(input(f'Choose a number between {start} and {end} : '))

    if choice == number:
        print('Your have success !!')
        break
    elif choice < number:
        print('this is lower !')
    else:
        print('this is greater !')

