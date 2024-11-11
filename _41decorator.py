# decorator
def hello():
    print('helllooooooooooooo')


great = hello()


great = hello
del hello
great()


def hello(func):
    func()


def greet():
    print('I\'s greeeettt')


hello(greet)

# higher order function
# as function as parameter
# or return a function
print()


def my_decorator(func):
    def wrap_func():
        print('do this before ')
        func()
        print('do this after ')
    return wrap_func


@my_decorator
def hello():
    print('hello!')


def hi():
    print('hiiii!')


hello()

hi()

my_decorator(hi)()


# make decorateur that accept func having any argument
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('do this before --')
        func(*args, **kwargs)
        print('do this after --')
    return wrap_func


@my_decorator
def hello(greeting):
    print(greeting)


hello('Hellooooooooo')
