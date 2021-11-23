def larger_than(a, b):
    """
    My Solution
    """
    if len(a) > len(b): return True
    elif len(a) == len(b):
        for i in range(len(a)):
            if a[i] > b[i]: return True
    return False 


def larger_than(a, b):
    """
    Correct solution
    """
    if len(a) > len(b): return True
    elif len(a) == len(b):
        for i in range(len(a)):
            if a[i] > b[i]: return True
    return False 