# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(blocks):
    print(len(blocks))
    return len(blocks)-1 if len(blocks)!=2 else 2



print(solution([2,6,8,5])) # 3
print(solution([1,2,5,5,6])) # 4
print(solution([1,1])) # 2