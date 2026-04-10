'''
Given an array of positive integers arr[], return the second largest element from the array. 
If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.
'''


def find(arr):
    if len(arr) < 2:
        return -1

    max_value = max(arr)
    second_max = -1

    for i in range(len(arr)):
        if arr[i] != max_value and arr[i] > second_max:
            second_max = arr[i]

    return second_max


print(find([3, 4, 9, 1, 8]))