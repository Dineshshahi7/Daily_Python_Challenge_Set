def findDuplicates(arr):
    duplicates = {}
    
    result = []
    for num in arr:
        if arr.count(num) == 2 and num not in result:
            result.append(num)
            
    return result

print(findDuplicates([1,2,2,3,3]))