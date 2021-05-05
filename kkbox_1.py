"""
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    a = 'aa'
    count_a = S.count('a')
    rewrite = ""
    if 'aaa' in S: return -1
    for i in S:
        if i != 'a':
            rewrite += a+i
    new_string = rewrite + a
    return new_string.count('a') - count_a
        

# print(solution('aabab')) # aabaabaa --> 3
print(solution('dog')) # aadaaoaagaa --> 8
print(solution('aa')) #  --> 0
print(solution('baaa')) #  --> -1
