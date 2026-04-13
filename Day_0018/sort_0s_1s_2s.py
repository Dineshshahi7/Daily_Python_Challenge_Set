def sort012(arr):
    count0 = 0
    count1 = 0
    count2 = 0

    # Count elements
    for num in arr:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    # Rewrite array
    i = 0

    for _ in range(count0):
        arr[i] = 0
        i += 1

    for _ in range(count1):
        arr[i] = 1
        i += 1

    for _ in range(count2):
        arr[i] = 2
        i += 1

    return arr


arr = [0, 1, 2, 0, 1, 2]
print(sort012(arr))