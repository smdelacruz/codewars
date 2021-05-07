# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    return int(*[x for x in range(0, len(A) + 1) if x not in A])


print(solution([2,3,1,5]))