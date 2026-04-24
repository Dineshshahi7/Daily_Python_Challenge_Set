'''
You are given an array arr[] of non-negative integers. You have to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

Examples:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.

Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.

Input: arr[] = [0, 0]
Output: [0, 0]
Explanation: No change in array as there are all 0s.
'''

# THis code is simple but not 100% correct for above question
def plusZerostoEnd(arr):
    zeros = []
    not_zeros = []
    result = []
    
    for num in arr:
        if num == 0:
            zeros.append(num)
        else:
            not_zeros.append(num)
    result = not_zeros + zeros
    
    return result
    
a = [1, 2, 0, 4, 3, 0, 5, 0]
print(plusZerostoEnd(a))


# The correct code for above question is :
def pushZerosToEnd(self, arr):
    j = 0  # position for next non-zero

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr