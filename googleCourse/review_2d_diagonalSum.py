# def diagonal_sum(given_2d):
#     """
#     my solution
#     """
#     total = 0
#     for i in range(len(given_2d)):
#         for j in range(len(given_2d[i])):
#             if i == j:
#                 total += given_2d[i][j]
#     return total

def diagonal_sum(given_2d):
    """
    correct solution
    """
    total = 0
    for i in range(len(given_2d)):
        total += given_2d[i][i]
    return total

print(diagonal_sum([[1,2,3,1], [4,5,6,1], [7,8,9,1],[9,8,7,2]]))
print(diagonal_sum([[1,2,3], [4,5,6], [7,8,9]]))