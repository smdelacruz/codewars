def solution(S):
    print(S)
    num = int(S.replace(S[0], "9"))
    print(S)
    div_by_3 =  [str(x).zfill(2) for x in range(0, num+1) if x % 3 == 0]
    oo = [i for i in div_by_3 if S[0] in i or S[0] in i]
    print(oo)

print(solution('23'))