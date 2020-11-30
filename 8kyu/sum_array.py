def sum_mix(arr):
    """
    Given an array of integers as strings and numbers, 
    return the sum of the array values as if all were numbers.
    Return your answer as a number.
    """
    return sum(int(x) for x in arr )

sum_mix([9, 3, '7', '3'])




def sum_array(arr):
    """
    Sum all the numbers of the array except the highest and the lowest element.
    ( The highest/lowest element is respectively only one element at each edge, 
    even if there are more than one with the same value!)

    If array is empty, null or None, or if only 1 Element exists, return 0.
    """
    if arr == None or len(arr) <= 2:
        return 0
    else:
        pp = [i for i in sorted(arr)]
        pp.pop(0)
        pp.pop(-1)
        return sum(pp)
        

def sum_array(arr):
    """
    Best Practice from code wars
    """
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0

sum_array([6, 2, 1, 8, 10])
