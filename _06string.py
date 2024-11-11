text= "this is a string"
text2= 'This is also a string'
print(text, text2)

message = '''
I am a string in more than
one lines
'''

print(message)

# string concatenation
firstname = 'John'
lastname = 'Doe'

full_name = firstname + ' ' + lastname
print(full_name)

# make error : print('hello ' + 10)
# number must be converted to string
print(str(100))
print(type(str(100)))

# Escape Sequence
weather = 'It \'s "kind of" sunny'
print(weather)
# tabulation
print('\t I am tabulated')
# new line
print('Single text \n in 2 line')

# formatted string
name = 'John'
age = 20
print(name)
print('Hi ' + name + ' you are ' + str(age) + ' old')
# print more easy
print(f'Hi {name} you are {age} year old')
# on python 2
print('Hi {} you are {} year old'.format(name, age))
print('Hi {1} you are {0} year old'.format(age, name))
print('Hi {n} you are {a} year old'.format(a=age, n=name))


# is a list of caracters
number = '0123456789'
print(number[5])

# score bracet accessing : sclicing
# [start:stop:step]

print(number[0:2])
print(number[0:8])
print(number[0:8:2])
print(number[2:])
print(number[:5])
print(number[:5])
print(number[-1])
print(number[7])
print(number[-10])
print(number[::-1]) # reverse

# string is immutable
# string element can be changed
# number[0] = '9' don't work

# string size 
great = 'Helloooooooooooooo'
print(len(great))

# string methods
quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be', 'me'))

# methods usualy work on the string value but not update it
print(quote)
quote_you = quote.replace('to', 'you')
print(quote_you)

 
