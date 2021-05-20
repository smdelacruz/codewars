# def solution(A):
#     """
#     My soltuion 2
#     30%
#     """
#     print("len", len(A))
#     if len(A) < 2 and len(A) != 0 : return A[0]
#     elif len(A) == 0: return A
#     smallest = 0
#     for i in range(len(A)-1):
#         # print("iiii", i)
#         right = sum(A[i+1:]) 
#         left = sum(A[:i+1])
#         suma = lambda x,y : abs(x - y)
#         hello = suma(right, left)
#         print("hello", hello)
#         if smallest == 0:
#             smallest = hello
#         elif hello < smallest:
#             smallest = hello
#     return smallest
 

# def solution(A):
#     """
#     My soltuion 3
#     53% O(n*n) test past but time complexity failed
#     """
#     print("len", len(A))
#     if len(A) < 2 and len(A) != 0 : return A[0]
#     elif len(A) == 0: return A
#     smallest = 1000000000000
#     for i in range(len(A)-1):
#         # print("iiii", i)
#         right = sum(A[i+1:]) 
#         left = sum(A[:i+1])
#         suma = lambda x,y : abs(x - y)
#         hello = suma(right, left)
#         print("hello", hello)
#         if hello < smallest:
#             smallest = hello
#     return smallest

def solution(A):         
    """
    from stackoverflow solution
    """ 
    s = sum(A)
    m = float('inf')
    print(m)
    left_sum = 0
    for i in A[:-1]:
        left_sum += i
        m = min(abs(s - 2*left_sum), m)
        print(m)
    return m

# print(solution([3,1,2,4,3]))
# print(solution([0,0,0,0,0]))
# print(solution([1,1,1,1,1]))
# print(solution([]))
# print(solution([0]))
# print(solution([20]))
# print(solution([-20]))
print(solution([1, 2, 3, 4, 2]))