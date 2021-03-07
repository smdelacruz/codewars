# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A = set(sorted(A))
    for i in range(min(A), max(A)+1):
        if i == max(A):
            return i + 1
        elif i not in A:
            return i if i > 0 else 1


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([-1, -3]))
print(solution([1, 2, 3]))
print(solution([5, 4, 3]))
    
