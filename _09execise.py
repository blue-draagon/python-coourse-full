# password checker
username = input('Your username : ')
password = input('Your password : ')

password_len = len(password)
hidden_password = '*' * password_len

print(f'{username}, your password {hidden_password} is {password_len} letters long.')