"""
kata
Your job is to implement a function which returns the last D digits of an integer N as a list.
Special cases:
If D > (the number of digits of N), return all the digits.
If D <= 0, return an empty list.

Examples:
N = 1
D = 1
result = [1]

N = 1234
D = 2
result = [3, 4]

N = 637547
D = 6
result = [6, 3, 7, 5, 4, 7]
"""

def solution(n,d):
    convertNumtoArr = [int(a) for a in str(n)] if d > 0 else []
    if len(convertNumtoArr) > d:
        return convertNumtoArr[-d:]
    else: return convertNumtoArr

"""
Other Codewarrior solution - simplified
def solution(n, d):
    return [int(c) for c in str(n)[-d:]] if d > 0 else []
"""


def test_solution():
    assert solution(1, 1) == [1]
    assert solution(0, 2) == [0]
    assert solution(1234, 0) == []
    assert solution(24134,-4) == []
    assert solution(1234, 2) == [3, 4]
    assert solution(637547, 6) == [6, 3, 7, 5, 4, 7]