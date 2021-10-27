"""
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    temp = ""
    counter = 1
    swap_counter = 0

    for i in S:
        if i!=temp:
            temp = i
            counter = 1
        elif counter <= 2:
            counter += 1
            if counter >= 3:
                swap_counter += 1
                counter = 0
    return swap_counter

print(solution('baaabbbba')) # 2
print(solution('baaaa')) # 1
print(solution('baaabbaabbba')) #  --> 2
print(solution('baabab')) #  --> 0
