"""
Very simple, given a number, find its opposite.
"""


def opposite(number):
    """
    My Solution
    """
  return abs(number) if number < 0 else number * -1

def opposite(number):
    """
    Best ; Clevel soltuion
    """
    return -number


print(opposite(-20))