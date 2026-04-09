'''
In this question, we'll use Regex to validate a password. You will be provided a string str which you have to validate.

The validation rules are as follows:

The string is valid only if it starts with lowercase characters, followed by special characters !@#$% followed by numbers.
In any other case the string is not valid.
'''

import re

password = input("Enter password: ")

pattern = r'^[a-z]+[!@#$%]+[0-9]+$'

if re.match(pattern, password):
    print("Valid")
else:
    print("Invalid")