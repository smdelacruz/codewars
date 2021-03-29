# Input:
#  chessboard: A 2-dimensional array that represents.  Example below.
#  [[1, 0, 0, 0],
#  [0, 1, 0, 0],
#  [0, 0, 0, 1],
#  [0, 0, 0, 0]]
# Returns:
#  True if none of the rooks can attack each other.
#  False if there is at least one pair of rooks that can attack each other.
def rooks_are_safe(chessboard):
    """
    CS Dojo solution
    """
    n = len(chessboard)
    print(n)
    # this loop will first loop on each rows
    for row_i in range(n):
        print("row_i", row_i)
        row_count = 0
        for col_i in range(n):
            print("col_i", col_i)
            print("chessboard[row_i][col_i]", chessboard[row_i][col_i])
            row_count += chessboard[row_i][col_i] #because 1=exist, and 0=does not exist, it will loop until added to 1
            print("row_count {}".format(row_count))
        if row_count > 1:
            print("here")
            return False
    # this loop will first loop on each column
    for col_i in range(n):
        print("col1", col_i)
        col_count = 0
        for row_i in range(n):
            print("row_i", row_i)
            print("chessboard[row_i][col_i]", chessboard[row_i][col_i])
            col_count += chessboard[row_i][col_i]
        if col_count > 1:
            print("its here")
            return False
    return True

print(rooks_are_safe([[1, 0, 0, 0],
[0, 1, 0, 0],
[0, 0, 0, 1],
[0, 0, 0, 0]]))

print(rooks_are_safe([[1, 3],
[1, 0]]))