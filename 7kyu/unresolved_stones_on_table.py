"""
There are some stones on Bob's table in a row, and each of them can be red, green or blue, indicated by the characters R, G, and B.

Help Bob find the minimum number of stones he needs to remove from the table so that the stones
in each pair of adjacent stones have different colours.

Examples:

"RGB RGB RGGB"   => 1 r= 3, G = 4, B = 3
"RGG RGB BRG RR"  => 3 r= 5, G = 4, B = 2
"RRRRGGGGBBBB" => 9 r=4, G = 4, B = 4
"""
def solution(s):
    """
    Unlocked the solution for this kata
    """
    st = [1 for i in range(1,len(s)) if s[i-1] == s[i]]
    return sum(st)


print(solution("RGBRGB"))# 0
print(solution("BGRBBGGBRRR"))# 4