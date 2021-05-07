# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    """My solution 1 O(n) 1.232s"""
    # holder = {}
    # for i in A:
    #     if i not in holder:
    #         holder[i] = 0
    #     holder[i] += 1
    # for k, v in holder.items():
    #     if v % 2 != 0:
    #         return k

    """My solution 2"""
    holder = {}
    for i in A:
        if i not in holder:
            holder[i] = 1
        elif i in holder:
            holder[i] = 0
    print(holder.values())
    print(holder[i])
    if holder.values() == 1:
        return holder[i]

print(solution([9,3,9,3,9,7,9]))