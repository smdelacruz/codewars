def solution(A):
    highest = max(A)
    lowest = min(A)
    # print(highest)
    # print(lowest)
    for i in range(lowest, highest):
        print(i)
        if highest <= 0 :
            return 1
        elif i not in A:
            return i
    return highest + 1


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([0, 100]))
# print(solution([1, 2, 3]))
# print(solution([-1, -3]))
# print(solution([1, 1]))