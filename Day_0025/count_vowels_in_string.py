'''
Problem: Count how many vowels (a, e, i, o, u) are in a string.

Example:

Input: "machine learning"
Output: 7
'''

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
            
    return count

print(count_vowels("machine learning"))