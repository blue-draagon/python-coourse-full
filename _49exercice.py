

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return [0, 1]
    fn = 0
    fn1 = 1
    for i in range(n+1):
        yield fn
        fn1, fn = fn1 + fn, fn1


for i in fib(100):
    print(i)
