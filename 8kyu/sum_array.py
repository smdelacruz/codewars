def sum_mix(arr):
    """
    Given an array of integers as strings and numbers, 
    return the sum of the array values as if all were numbers.
    Return your answer as a number.
    """
    return sum(int(x) for x in arr )

sum_mix([9, 3, '7', '3'])