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
    for i in range(10000000):
        pass


long_time()
