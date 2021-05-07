"""# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
"""
def solution(X, Y, D):
    """
    My solution 1
    Detected Time complexity O(Y-X)
    44%
    """
    counter = 0
    while X < Y:
        X += D
        counter +=1
    return counter


import math
def solution(X, Y, D):
    """
    My solution 2
    Detected Time complexity
    O(1)
    100 %
    """
    return math.ceil((Y-X) / D)


print(solution(10,85,30))
print(solution(10,10,-30))
