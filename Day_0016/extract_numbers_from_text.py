'''
Regular expressions are extremely helpful in extracting useful information from loads of text. Regular expressions work on pattern-matching techniques. Extracting phone-number, validating passwords, and extracting images from web-pages are but a few examples of regex usage.

In this question, we'll learn the use of Regex in Python. You will be provided a string str in which you have to find all the numbers and print them.

Note: In Python, you need to import re module to use regex
'''

import re

def extract_numbers(str):
    numbers = re.findall(r'\d+', str)
    print(*numbers)


str = "asdasd123asmdasdk34234kfdsd34sdfk5"
extract_numbers(str)