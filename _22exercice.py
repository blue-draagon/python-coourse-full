# count element in list
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

letters_count = dict()

for letter in lorem:
    value = letters_count.get(letter)
    if value:
        letters_count.update({letter: value+1})
    else:
        letters_count.update({letter: 1})
        

for letter, count in letters_count.items():
    print(f'letter {letter} is present {count} time in paragraphe')