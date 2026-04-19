'''
Given an array arr of non-negative integers and an integer target, the task is to count all subsets of the array whose sum is equal to the given target.

Examples:

Input: arr[] = [5, 2, 3, 10, 6, 8], target = 10
Output: 3
Explanation: The subsets {5, 2, 3}, {2, 8}, and {10} sum up to the target 10.

Input: arr[] = [2, 5, 1, 4, 3], target = 10
Output: 3
Explanation: The subsets {2, 1, 4, 3}, {5, 1, 4}, and {2, 5, 3} sum up to the target 10.

Input: arr[] = [5, 7, 8], target = 3
Output: 0
Explanation: There are no subsets of the array that sum up to the target 3.

Input: arr[] = [35, 2, 8, 22], target = 0
Output: 1
Explanation: The empty subset is the only subset with a sum of 0.
'''

def count_subsets(arr, target):
    dp = [0] * (target + 1)
    dp[0] = 1 

    for num in arr:
        for j in range(target, num - 1, -1):
            dp[j] += dp[j - num]

    return dp[target]


print(count_subsets([5, 2, 3, 10, 6, 8], 10))  # 3
print(count_subsets([2, 5, 1, 4, 3], 10))      # 3
print(count_subsets([5, 7, 8], 3))             # 0
print(count_subsets([35, 2, 8, 22], 0))        # 1