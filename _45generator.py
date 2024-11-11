# generate things over the time
# iterable __iter__ iterate
# generator is a subset of a iterable

def generator_func(num):
    for i in range(num):
        yield i * 2


# for item in generator_func(1000):
#     print(item)

g = generator_func(100)
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# next ending

g = generator_func(1)
print(g)
print(next(g))
# print(next(g)) generate eror
