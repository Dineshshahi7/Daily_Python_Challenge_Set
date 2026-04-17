'''
Given an array arr[] of integers and another integer target. Determine if there exist two distinct indices 
such that the sum of their elements is equal to the target.

Examples:

Input: arr[] = [0, -1, 2, -3, 1], target = -2
Output: true
Explanation: arr[3] + arr[4] = -3 + 1 = -2

Input: arr[] = [1, -2, 1, 0, 5], target = 0
Output: false
Explanation: None of the pair makes a sum of 0

Input: arr[] = [11], target = 11
Output: false
Explanation: No pair is possible as only one element is present in arr[]
'''
def twosum(arr, target):
    seen = set()
    
    for num in arr:
        complement = target - num
        
        if complement in seen:
            return True
        
        seen.add(num)
    return False


print(twosum([0, -1, 2, -3, 1], -2))
print(twosum([1, -2, 1, 0, 5], 0))


'''
Explaination

Create an empty set
seen = set()
A set stores unique values
We’ll use it to keep track of numbers we’ve already seen
Helps us check values quickly (in O(1) time)

🔹 Loop through each number
for num in arr:
Goes through each element in the array one by one
num represents the current element

🔹 Find required pair value
complement = target - num
We calculate what number is needed to reach the target
Example:
If target = 10 and num = 3
Then complement = 7
So we check: Have we already seen 7?

🔹 Check if complement exists
if complement in seen:
    return True
If the needed number is already in the set:
That means we found two numbers whose sum = target ✅
Immediately return True

🔹 Store current number
seen.add(num)
If no pair found yet, store current number in the set
So future elements can check against it

🔹 If no pair found
return False
If loop finishes and no pair matches target
Return False
'''
