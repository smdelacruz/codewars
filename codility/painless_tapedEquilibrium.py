# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    """
    My soltuion
    """
    smallest = 0
    for i in range(len(A)):
        right = A[i+1:] if i != A[-1] else A[i]
        left = A[:i+1]
        hello = sum(right) if type(right) != int else right
        current = abs(sum(left) - hello)
        if smallest == 0 or smallest >= current:
            smallest = current
    return smallest


print(solution([3,1,2,4,3]))
print(solution([0,0,0,0,0]))
print(solution([1,1,1,1,1]))
print(solution([]))
print(solution([0]))
print(solution([20]))
print(solution([-20]))
print(solution([20, 0]))