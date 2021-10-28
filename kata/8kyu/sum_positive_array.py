def positive_sum(arr):
    """
    My solution
    You get an array of numbers, return the sum of all of the positives ones.
    Example [1,-4,7,12] => 1 + 7 + 12 = 20
    """
    p = sum([p for p in arr if p > 0])
    print(p)


positive_sum([1,2,3,4,5])