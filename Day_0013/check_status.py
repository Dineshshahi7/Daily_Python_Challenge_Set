''' #Task
Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return False.
'''


class Solution:
    def checkStatus(self, a, b, flag):
        if flag == False:
            if (a >= 0 and b < 0) or (a < 0 and b >= 0):
                return True
            else:
                return False
        else:
            if a < 0 and b < 0:
                return True
            else:
                return False


# create object (instance)
obj = Solution()

# take input from user
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
flag = input("Enter flag (True/False): ")

# convert string input to boolean
if flag == "True":
    flag = True
else:
    flag = False

# call function
result = obj.checkStatus(a, b, flag)

# print result
print("Output:", result)