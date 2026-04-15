'''
Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, and another number occurs twice in the array, find both the duplicate number and the missing number.

Examples:

Input: arr[] = [2, 2]
Output: [2, 1]
Explanation: Repeating number is 2 and the missing number is 1.
Input: arr[] = [1, 3, 3] 
Output: [3, 2]
Explanation: Repeating number is 3 and the missing number is 2.
Input: arr[] = [4, 3, 6, 2, 1, 1]
Output: [1, 5]
Explanation: Repeating number is 1 and the missing number is 5.
'''

def findTwoElement(self, arr):
    n = len(arr)
    freq = [0] * (n + 1)

    for num in arr:
        freq[num] += 1

    duplicate = -1
    missing = -1

    for i in range(1, n + 1):
        if freq[i] == 2:
            duplicate = i
        elif freq[i] == 0:
            missing = i

    return [duplicate, missing]


print(findTwoElement([4,2,3,6,1,1]))