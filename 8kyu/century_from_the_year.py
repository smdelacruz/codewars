"""
The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.

Task :
Given a year, return the century it is in.

Input , Output Examples ::
centuryFromYear(1705)  returns (18)
centuryFromYear(1900)  returns (19)
centuryFromYear(1601)  returns (17)
centuryFromYear(2000)  returns (20)
Hope you enjoy it .. Awaiting for Best Practice Codes
"""

def century(year):
    """
    My solution: Wrong.. revealed the answer
    """
    return year // 100


import math
def century(year):
    """
    Best practice solution
    """
    return math.ceil(year // 100)

print(century(1705))
print(century(1900))
print(century(1601))
print(century(2000))