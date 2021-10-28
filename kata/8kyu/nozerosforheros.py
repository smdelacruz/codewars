"""
Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.
"""

def no_boring_zeros(n):
    """
    My solution
    """
    if n == 0:
        return n
    else:
        to_int = str(n).rstrip('0')
        return int(to_int)

def no_boring_zeros(n):
    """
    Best Practice ; Clever
    """
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0


print(no_boring_zeros(1450))
print(no_boring_zeros(0))