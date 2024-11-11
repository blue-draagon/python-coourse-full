# let the script continue running after errors
while True:
    try:
        age = int(input('Your age : '))
        print(age)
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('the number must be higher than 0')
    else:
        print('thank you!')
        break


# by limit type of error we make
#  sur to handle the exception we want

def func(num):
    try:
        return num ** 2
    except TypeError as err:
        print(f'Error : {err}')


print(func('2'))


# handler two error type
def func(num):
    try:
        return 10 / num
    except (TypeError, ZeroDivisionError) as err:
        print(f'Error : {err}')


print(func(0))


# using finally
while True:
    try:
        age = int(input('Your age : '))
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('the number must be higher than 0')
    else:
        print('thank you!')
        break
    finally:
        print('I am allways done')

# finally run whatever happen
