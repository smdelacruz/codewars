def reverse_seq(n):
    """
    Build a function that returns an array of integers from n to 1 where n>0.

    Example : n=5 >> [5,4,3,2,1]
    """
    return sorted([i for i in range(1, n+1)],reverse=True)


def reverseseq(n):
    """
    best solution 
    """
    return list(range(n, 0, -1))