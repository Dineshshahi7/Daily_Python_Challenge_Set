'''
Python has a lot of string methods that can be used to manipulate the strings like converting to lowercase, capitalizing,
trimming the spaces and so on.

In this question, we'll take a look at inbuilt string methods like title(), swapcase(), find(), strip().
You'll be given a string str and x, you'll perform various operations on them.
'''

def trim(str):
    return str.strip()

def exists(str,x):
    return str.find(x)

def titleIt(str):
    return str.title()

def casesSwap(str):
    return str.swapcase()