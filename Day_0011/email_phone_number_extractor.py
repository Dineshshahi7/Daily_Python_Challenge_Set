'''
# Email & Phone Number Extractor (Regex Project)
- Create a Python program that can extract emails and phone numbers from a paragraph using regular expressions.

i) The program should:
- Take a long text paragraph as input
- Extract all email addresses
- Extract all phone numbers
- Print them separately
'''

import re

email = input("Enter email: ")
phone = input("Enter phone number: ")

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
phone_pattern = r'^\d{10}$'

if re.match(email_pattern, email):
    print("Email valid")
else:
    print("Email not matching")

if re.match(phone_pattern, phone):
    print("Phone number valid")
else:
    print("Phone number not matching")
