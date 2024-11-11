import re

email_regex = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
email_pattern = re.compile(email_regex)
print(email_pattern.search('test@test.com'))


password_pattern = re.compile(r"[A-Za-z0-9@#_]{8,}\d")
print(password_pattern.search('@25salamhello8'))
