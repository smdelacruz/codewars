# def count_negatives(input):
#     """
#     my solution O(n^2)
#     """
#     n = len(input)
#     counter = 0
#     for i in range(n):
#         for j in range(n):
#             if input[i][j] < 0:
#                 counter+=1
#     return counter


def count_negatives(given_array):
    """
    Correct solution
    """
    row_i = 0
    col_i = len(given_array[0]) - 1 #start at the top-right most corner
    counter = 0
    
    while col_i >= 0 and row_i < len(given_array):
        if(given_array[row_i][col_i]) < 0:
            counter += (col_i + 1)
            row_i += 1
        else: 
            col_i = col_i - 1
    return counter


# print(count_negatives([[-4,-3,-1,1],
#                       [-2,-2,1,2],
#                       [-1,1,2,3],
#                       [1,2,4,5]]))
print(count_negatives([[-2,0],[-1,0]]))