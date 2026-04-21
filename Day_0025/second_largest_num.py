'''
Problem: Given a list of numbers, find the second largest unique number.

Example:

Input: [10, 20, 4, 45, 99, 99]
Output: 45
'''

def second_largest(nums):
    unique_nums = list(set(nums))
    unique_nums.sort()
    
    if len(unique_nums) < 2:
        return None
    
    return unique_nums[-2]


print(second_largest([10, 20, 4, 45, 99, 99]))