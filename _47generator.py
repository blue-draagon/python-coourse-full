def my_for(iterable):
    iterator = iter(iterable)
    while 1:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


my_for([1, 2, 3, 4, 5])
