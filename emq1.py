# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    for x in ["AB", "BA", "CD", "DC"]:
        if x in S:
            S = S.replace(x, "")
    return S

print(solution("CBACD")) # C
print(solution("CABABD")) # empty
print(solution("ACBDACBD")) # ACBDACBD