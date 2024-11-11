from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'took  {end - start} s')
        return result

    return wrapper


@performance
def long_time():
    print('lt 1')
    for i in range(10000000):
        i*5


@performance
def long_time2():
    print('lt 2')
    for i in list(range(10000000)):
        i*5


long_time()
long_time2()

# generator make more performance
