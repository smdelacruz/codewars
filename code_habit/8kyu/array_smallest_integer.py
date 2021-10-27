"""
Given an array of integers your solution should find the smallest integer.
"""

def find_smallest_int(arr):
    """
    My solution
    """
    return sorted(arr)[0]


def findSmallestInt(arr):
    """BEst solution from other code warriors"""
    return min(arr)

print(find_smallest_int([78, 56, 232, 12, 11, 43]))
print(find_smallest_int([78, 56, -2, 12, 8, -33]))