def subarray_sum(arr, target):
    left = 0
    current_sum = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        # Shrink window if sum becomes greater than target
        while current_sum > target and left <= right:
            current_sum -= arr[left]
            left += 1

        # Check if target is found
        if current_sum == target:
            return [left + 1, right + 1]   # 1-based indexing

    return [-1]


# Example
arr = [1, 2, 3, 7, 5]
target = 12

print(subarray_sum(arr, target))