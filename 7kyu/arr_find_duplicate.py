def find_dup(arr):
    p = []
    for i in arr:
        p.append(i)
        if i in p:
            print(i)
            return i



find_dup([5, 4, 3, 2, 1, 1]) #1
find_dup([1, 3, 2, 5, 4, 5, 7, 6]) #5