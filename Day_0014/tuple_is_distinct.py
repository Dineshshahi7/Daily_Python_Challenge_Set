''' 
Given a tuple arr , print "True" if all elements of tuple are different otherwise print "False".

A tuple is a collection of items that are ordered and unchangeable.
'''

# Take numbers from user separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# Convert input into tuple of integers
arr = tuple(map(int, user_input.split()))

arr_len = len(arr)
set_len = len(set(arr))

if arr_len == set_len:
    print("True")
else:
    print("False")