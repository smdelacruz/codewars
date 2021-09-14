# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # return int(*[x for x in range(0, len(A) + 1) if x not in A])
    """
    My solution 1
    O(N**2)
    50%
    """
    # if A:
    #     missing = 1
    #     for x in range(1, len(A)+1):
    #         print("missin", missing)
    #         if missing not in A: return x
    #         missing += 1
    #     print("final missing", missing)
    #     return missing
    # else: return A
    # missing = 1
    # for x in range(1, len(A)+1):
    #     if missing not in A: return x
    #     missing += 1
    # return missing

    return [x+1 for x in range(1, len(A)+1) if x not in A ]
    # print(m)


    
# print(solution([2,3,1,5]))
# print(solution([1,2,3,4]))
print(solution([1,2,3,4]))
print(solution([2,3,4,5]))
# print(solution(1))
print(solution([0]))
# print(solution([8]))