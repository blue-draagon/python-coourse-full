while True:
    try:
        age = int(input('Your age : '))
        10/age
        raise Exception('my raise error')
    except ValueError:
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print('the number must be higher than 0')
        break
    else:
        print('thank you!')
    finally:
        print('I am allways done')
    print('can you hear me?')
