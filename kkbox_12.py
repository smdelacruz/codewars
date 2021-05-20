# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    pairs = []
    for i in range(1,len(S)):
        if len(S[:i+1]) > 2:
            pairs.append(int(S[i-1:i+1]))
        else:
            pairs.append(int(S[:i+1]))
    return max(pairs) if len(pairs) != 0 else pairs


print(solution("505585698472340992"))
print(solution("10101"))
print(solution("88"))
print(solution([]))