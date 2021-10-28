def flip(d, a):
    """
    My solution
    example:
    flip('R', [3, 2, 1, 2])     =>  [1, 2, 2, 3]
    flip('L', [1, 4, 5, 3, 5])  =>  [5, 5, 4, 3, 1]
    """
    return sorted(a) if d == 'R' else sorted(a, reverse=True)

def flip(d,a):
    """
    Best solution on codewars
    """
    return sorted(a, reverse=d=='L')



flip('R', [3, 2, 1, 2])
flip('L', [1, 4, 5, 3, 5])