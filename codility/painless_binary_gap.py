def solution(N):
    """
    My solution 1

    binary = str(format(N, 'b'))
    store_ones_indx = []
    diff = []
    for idx,v in enumerate(binary, 1):
        if v == '1':
            store_ones_indx.append(idx)
    for i in range(len(store_ones_indx)):
        try:
            hello = store_ones_indx[i+1] - store_ones_indx[i] - 1
            diff.append(hello)
        except: pass
    return max(diff) if diff else 0
    """

    """My solution 2"""
    binary = str(format(N, 'b'))
    zero_counter = 0
    highest_zero_count = 0
    for i in binary:
        if i == '1':
            if zero_counter > highest_zero_count:
                highest_zero_count = zero_counter
            zero_counter = 0
        else:
            zero_counter +=1
    return highest_zero_count


# print(solution(9)) # 2
# print(solution(5)) # 3
# print(solution(20)) # 1
# print(solution(15)) # 0
print(solution(1041)) # 5
print(solution(32)) # 0
# print(solution(328)) #2
print(solution(6291457)) #20



