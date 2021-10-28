def grow(arr):
    """
    Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
    [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
    """
    prod = 1
    for i in arr:
        prod = prod * i
    return prod

"""
Voted as best solution
"""
from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)



grow([1, 2, 3])
grow([4, 1, 1, 1, 4])
grow([2, 2, 2, 2, 2, 2])