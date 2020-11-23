def is_divisible(n, x, y):
    """
    My solution
    Create a function that checks if a number n is divisible by two numbers x AND y.
    All inputs are positive, non-zero digits.
    Examples:
    1) n =   3, x = 1, y = 3 =>  true because   3 is divisible by 1 and 3
    3) n = 100, x = 5, y = 3 => false because 100 is not divisible by 3
    """
    print( True if n % x == 0 and n % y == 0 else False)


def is_divisible(n,x,y):
    """
    Other solution in codewars
    """
    return n % x == 0 and n % y == 0


is_divisible(8,3,4)