'''
Here we'll talk about the novel and perhaps tantalizing concept of slicing. Slicing is the process through which you can extract some
continuous part of a string. For example: string is "python", let's use slicing in this. Slicing can be done as:

a. string[0:2] = py (Slicing till index 1)
b. string[0:] = python (Slicing till last index)
c. string[0:4] = pyth (Slicing till index 3)
d. string[0:-2] = pyth (Slicing till index -3).
Note: -1 indexing starts from last of any string.

Now, lets look into this through a question. Given a string of braces named bound_by, and a string named tag_name. The task is to print a new string such that tag_name is in the middle of bound_by.

Example 1:

Input: 
bound_by = [[]], tag_name = tag
Output:
[[tag]]
Example 2:

Input: 
bound_by = <>, tag_name = body
Output:
<body>
'''


def join_middle(bound_by, tag_name):
  
  return bound_by[0 : len(bound_by) // 2] + tag_name + bound_by[len(bound_by)//2 :]


print(join_middle('[[]]', 'Dinesh'))
print(join_middle('<<>>>', 'Shahi'))