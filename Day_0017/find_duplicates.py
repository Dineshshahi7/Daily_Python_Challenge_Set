'''
Given a sorted array arr[] having 10 elements which contain 6 different numbers in which only 1 number is repeated five times. Your task is to find the duplicate number using two comparisons only.

Examples:

Input: arr[] = [1, 1, 1, 1, 1, 5, 7, 10, 20, 30]
Output: 1
Input: arr[] = [1, 2, 3, 3, 3, 3, 3, 5, 9, 10]
Output: 3
'''

def find_duplicate(arr):
    # First comparison
    if arr[4] == arr[5]:
        return arr[4]

    # Second comparison
    if arr[0] == arr[4]:
        return arr[4]
    else:
        return arr[5]

arr = list(map(int, input("Enter 10 sorted numbers: ").split()))

if len(arr) != 10:
    print("Please enter exactly 10 elements.")
else:
    print("Duplicate number is:", find_duplicate(arr))
    
    
'''
Explaination:
Because the array is sorted, and exactly one number is repeated 5 times, we can solve this in only 2 comparisons.
The repeated number occupies 5 continuous positions.
For an array of size 10, a block of length 5 must be in one of these positions

So we first check the middle two elements:
arr[4] == arr[5]
If they are equal, then the duplicate block lies somewhere from 1 to 8, so the repeated number

Not Equal
Then the repeated block must be either:
0 to 4
or
5 to 9

Now use the second comparison:
arr[0] == arr[4]
If true → duplicate is arr[4]
Else → duplicate is arr[5]
'''
