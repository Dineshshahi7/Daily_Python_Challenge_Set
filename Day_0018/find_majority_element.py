def MajorityElement(arr):
    mid = len(arr) / 2
    
    for num in arr:
        if arr.count(num) > mid:
            return num
    
    return -1
        
        
print(MajorityElement([7]))
print(MajorityElement([1, 1, 2, 1, 3, 5, 1]))
