# Modify the following function:
def diagonal_sum(given_2d):
    """
    My solution
    """
    the_sum = 0
    for row in range(len(given_2d)):
        for i in range(len(given_2d[row])):
            if row == i:
                the_sum += given_2d[row][i]
    return the_sum

def diagonal_sum(given_2d):
    """
    CS Dojo solution
    """
    the_sum = 0
    for row in range(len(given_2d)):
        the_sum += given_2d[row][row]
    return the_sum


print(diagonal_sum([[1, 0],
              [0, 1]]))
print(diagonal_sum([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]))
