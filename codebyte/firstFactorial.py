"""
For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. 
Examples:

Input: 4
Output: 24

Input: 8
Output: 40320
"""

def FirstFactorial(num):
    new_num = 1
    for i in range(num, 1, -1):
        new_num *= i
    return new_num


# keep this function call here 
print(FirstFactorial(4))