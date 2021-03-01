"""
In this Kata, you will be given a string that has lowercase letters and numbers. Your task is to compare the number groupings and return the largest number. Numbers will not have leading zeros.

For example, solve("gh12cdy695m1") = 695, because this is the largest of all number groupings.

Good luck!
"""

import re


def solve(s):
    """
    BEst practice solution
    """
    return max(map(int,re.findall(r"(\d+)", s)))


def solve(s):
    """
    Most clever solution
    """

    largest = 0
    number = 0
    
    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)
            if largest < number:
                largest = number
        else:
            number = 0
            
    return largest

print(solve('gh12cdy695m1'))#695
# print(solve('2ti9iei7qhr5'))#9
# print(solve('vih61w8oohj5'))#61
# print(solve('f7g42g16hcu5'))#42