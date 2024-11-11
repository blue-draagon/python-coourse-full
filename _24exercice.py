def highest_even(li:list):
    li.sort()
    li.reverse()
    for item in li:
        if item % 2 == 0:
            print(f'{item} is the highest even of list {li}')
            return
        

highest_even([15,30,50,60,10,16,11,51,71])