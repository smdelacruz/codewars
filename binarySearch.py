
"""
Search the target on the array and return the index/location
"""
import math
def search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (right + left) / 2
        print(left, right, middle)
        if arr[middle] == target:
            return middle
        elif target > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return -1


print(search([-2,3,4,7,8,9,11,13], 13))