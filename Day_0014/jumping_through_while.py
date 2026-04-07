'''
Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).
Note: The increasing order means the next elements must greater than previous element, but in ascending order next elements may be same or greater
increasing order = [1,2,4,5,6,8,9]
ascenindg order = [1,2,2,3,4,4,5]
'''
# Function to print x in increasing order
def printIncreasingPower(x):
    start = 1
    jump = 1

    # Loop to jump in powers of 2
    while (jump <= x):
        print(jump, end=" ")
        start += 1
        jump = start**2