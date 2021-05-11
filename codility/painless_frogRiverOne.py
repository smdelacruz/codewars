# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(X, A):
#     """
#     My soltiion1
#     18%
#     """
#     for i, v in enumerate(A):
#         print("{}=={}".format(X, v))
#         if X == v:
#             return i
#     return -1

def solution(X, A):
    """
    My soltiion1
    18%
    """
    for i, v in enumerate(A):
        print("{}=={}".format(X, v))
        if X == v:
            return i
    return -1

print(solution(5, [1,3,1,4,2,3,5,4]))
print(solution(5, [0]))
print(solution(2, [2,2,2,2,2]))