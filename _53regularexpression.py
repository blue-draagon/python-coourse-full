import re

string = 'search inside of this text please!'
# finding inside text
print('search' in string)

# finding using regular expression
print(re.search('this', string))

# re search return object
result = re.search('this', string)
print(type(result))
# find location
print(result.span())
# starting and ending
print(result.start())
print(result.end())

# return the matching element
print(result.group())

# if not found result is None
print(re.search('notexist', string))

# use compiled pattern
pattern = re.compile('text')
# search pattern directly inside de string
result = pattern.search(string)
print(result)

# getting all occurences
pattern = re.compile('e')
print(pattern.findall(string))

# check if string contains only pattern
pattern = re.compile(string)
print(pattern.fullmatch(string))
pattern = re.compile(string+' some thing')
print(pattern.fullmatch(string))

# match similar like search
regex = r"([a-zA-Z]).([a])"
# r mean use this string like it is
pattern = re.compile(regex)
result = pattern.search(string)
print(result)
print(result.group())
print(result.group(1))
print(result.group(2))

# start with ^
# end with $
