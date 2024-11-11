# test by equality
print(True == 1)
print('1' == 1)
print([1] == 1)
print(10 == 10.0)
print([] == [])

print('-----------------------')
# test by type and equality
print(True is 1)
print('1' is 1)
print([1] is 1)
print(10 is 10.0)
print([] is [])
# is check object are same location in memery

a = dict()
b = dict()
print(a is b)
# because pointed to 2 different place of memory