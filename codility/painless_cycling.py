# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def rotateList(A,K):
    """
    My solution 1
    working on some arrays but wrong
    # print(rotateList([3, 8, 9, 7, 6], 3))#[9, 7, 6, 3, 8]
    # print(rotateList([0,0,0], 1)) #[0,0,0]
    # print(rotateList([1, 2, 3, 4], 4)) #[1234]
    # print(rotateList([], 4)) #[]
    25%
    """
    print(len(A))
    print(K-1)
    if len(A) > K:
        A[:]=A[K-1:len(A)]+A[0:K-1]
    return A

def rotateList(A,K):
    """
    My solution 2
    after several try
    62% runtime error on some tests
    """
    return [A[x-K] for x in range(len(A))]


def rotateList(A,K):
    """
    My solution 3
    if statement was from google
    75%
    """
    if len(A) < 2 or len(A) == K:
        return A
    else:
        return [A[x-K] for x in range(len(A))]


print(rotateList([3, 8, 9, 7, 6], 3))#[9, 7, 6, 3, 8]
print(rotateList([0,0,0], 1)) #[0,0,0]
print(rotateList([1, 2, 3, 4], 4)) #[1234]
print(rotateList([], 4)) #[]
print(rotateList([-3, -8, -9, -7, -6], 2)) #[-7,-6,-3,-8,-9]
print(rotateList([5], 2)) #5
print(rotateList([1, 1, 2, 3, 5], 42)) # [3, 5, 1, 1, 2]

# print(solution([3, 8, 9, 7, 6], 3))  #[9, 7, 6, 3, 8]
    #[3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    # [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    # [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
