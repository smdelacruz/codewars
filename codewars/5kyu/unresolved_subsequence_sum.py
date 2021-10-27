"""
get the subsequence of array what will result to value on s, 
output is the number of arrays that has result of s

arr = [1, 2, 3, -3, -2, -1], s = 0 -> 3 
# [3, -3], [2, 3, -3, -2], [1, 2, 3, -3, -2, -1]
------------------------------------------------------------
arr = [1, 5, -2, 4, 0, -7, -3, 6], s = 4 -> 4
# [1, 5, -2], [4], [4, 0], [1, 5, -2, 4, 0, -7, -3, 6]
------------------------------------------------------------
arr = [9, -2, -5, 8, 6, -10, 0, -4], s = -1 -> 2
# [-5, 8, 6, -10], [-5, 8, 6, -10, 0]
"""
# solution from kata
from collections import defaultdict
from itertools import accumulate

def subsequence_sums(arr, s):
    res, memo = 0, defaultdict(int)
    for x in accumulate(arr, initial=0):
        res += memo[x-s]
        memo[x] += 1
    return res


# solution from kata
from collections import defaultdict

def subsequence_sums(arr, s):
    sums_count = defaultdict(int)
    sums = 0
    count = 0
    for i in arr:
        sums += i
        if sums == s:
            count += 1
        if sums - s in sums_count:
            count += sums_count[sums - s]
        sums_count[sums] += 1
    return count

# print(subsequence_sums([1, 2, 3, -3, -2, -1], 0)) #3    
# print(subsequence_sums([1, 5, -2, 4, 0, -7, -3, 6], 4)) #4
print(subsequence_sums([4, 0], 4)) #4
# print(subsequence_sums([9, -2, -5, 8, 6, -10, 0, -4], -1)) #4



