def rooks_are_safe(rooks):
    n = len(rooks)
    for i in range(n):
        row_counter = 0
        col_counter = 0
        for j in range(n):
            if rooks[i][j] == 1:
                row_counter+=1
            if rooks[j][i] == 1: 
                col_counter+=1
        if (row_counter > 1) or (col_counter > 1): return False
    return True

print(rooks_are_safe([[0,0,1,0],
                      [1,0,0,0],
                      [1,0,0,0],
                      [0,0,0,1]]))
print(rooks_are_safe([[0,1], [0,1]]))