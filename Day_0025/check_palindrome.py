'''
Problem: Check if a string is a palindrome (same forward and backward), ignoring spaces.

Example:

Input: "nurses run"
Output: True
'''

def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("nurses run"))