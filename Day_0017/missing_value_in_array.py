'''
# You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

Examples:
Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.

Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.

Input: arr[] = [1]
Output: 2
Explanation: Only 1 is present so the missing element is 2.
'''



def messingnumber(arr):
    if len(arr) == 1:
        return arr[0]+1
    
    else:
        min_val = min(arr)
        max_val = max(arr)
        
        for i in range(min_val, max_val+1):
            if i not in arr:
                return i
           
x = messingnumber([4,6,9,8,7])
print(x)


'''
# Problem in your code
Above code works for some cases, but it has two important problems:

1. It fails when the missing number is at the beginning
2. It is inefficient because i not in arr checks the whole list every time
3. range(min_value, max_value+1), it checks only between the minimum and maximum values present in the array. But the missing number can be 1 or n.
'''

'''
# Better Approach (Using Sum Formula)

The best and easiest way is:
We know sum of numbers from 1 to n is: n(n+1)/2

Then subtract the sum of array elements.

But one important thing is this method always works with the number which starts from 1

'''

def messingNum(arr): 
    n = len(arr) + 1 
    total_sum = n * (n + 1) // 2 
    actual_sum = sum(arr) 
    return total_sum - actual_sum 

y = messingNum([1, 5, 3, 4]) 
print(y)

