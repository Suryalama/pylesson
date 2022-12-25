import re

is_phone_number=re.compile(r'\d\d\d')
code=is_phone_number.search('My code is 456')
print(code.group())

