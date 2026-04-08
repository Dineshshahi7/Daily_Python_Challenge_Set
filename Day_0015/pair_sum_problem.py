'''
Given a list arr[], of positive integers, and an integer sum. The task is to check if any pair exists in the array whose sum is equal to the given sum. If such a pair exists return true, otherwise, return false.

Example:

Input: arr[] = [1, 2, 3, 3, 5], sum = 8 
Output: true
Explanation: Pair with sum 8 is present in the array which is (3, 5).
Input: arr[] = [3, 2, 5], sum = 6 
Output: false
Explanation: No such pair exists in the array.
'''

def pair_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False

print(pair_sum([1,2,3,3,5], 8))
print(pair_sum([3,2,5], 6))


'''
Best optimized solution (using set)
This is the best approach because it works in O(n) time.
'''

def pair_sum(arr, target):
    seen = set()

    for num in arr:
        complement = target - num

        if complement in seen:
            return True

        seen.add(num)

    return False


arr = [1, 2, 3, 3, 5]
target = 8

print(pair_sum(arr, target))