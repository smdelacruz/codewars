"""
Unsolved
The status of each element of an array of integers can be determined by its position in the array and the value of the other elements in the array. The status of an element E in an array of size N is determined by adding the position P, 0 <= P < N, of the element in the array to the number of array elements in the array that are less than E.

For example, consider the array containing the integers: 6 9 3 8 2 3 1. The status of the element 8 is 8 because its position is 3 and there are 5 elements in the array that are less than 8.

You will return the elements of the original array from low to high status order. In the event there is a tie for status of two or more elements, you will output them in order of appearance in the array.

EXAMPLE:

status([6, 9, 3, 8, 2, 3, 1]) = [6, 3, 2, 1, 9, 3, 8]
"""


def status(nums):
    #let's crank some code!
    return ""


print(status([6,9,3,8,2,3,1]))#,[6,3,2,1,9,3,8]))
print(status([14,-3,4,6,9,10,-2,4,0]))#, [-3,4,-2,14,6,9,4,0,10])
print(status([5 ,5 ,5 ,8 ,7 ,-2 ,-2 ,-3 ,1 ,9, 8 ,3 ,-3, 4 ,-4 ,6 ]))#[5, -2, -3, 5, -2, 5, 1, -3, -4, 8, 7, 3, 4, 8, 9, 6]))