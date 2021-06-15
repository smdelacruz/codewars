"""
Problem:
input = [0, 0, 1, 1]
return [0, 1, x, x]
x need to be Unique number
like [0, 1, 2, 4]
"""

def unique(arr):
    len_arr = len(arr)
    p  = list(set(arr))
    max_num = max(p)
    for i in range(len(p),len_arr):
        max_num += 1
        if max_num not in p:
            p.append(max_num)
            max_num += 1
    return p
print(unique([0, 0, 1, 1]))
print(unique([-1, -2, -3, -4]))

