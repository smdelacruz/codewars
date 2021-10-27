def two_sort(array):
    """
    My solution
    You will be given a vector of strings. 
    You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) 
    and then return the first value.
    
    The returned value must be a string, and have "***" between each of its letters.
    You should not remove or add elements from/to the array.
    """
    result = "***".join(a for a in [o for o in sorted(array)][0])
    return result


def two_sort(array):
    """
    Best soltuion from codewars
    """
    return '***'.join(min(array))


def two_sort(arr):
    """
    Other solution from codewars
    """
    return '***'.join(sorted(arr)[0])


    
two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"])