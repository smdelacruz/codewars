def digitize(n):
    """
    Given a random non-negative number, 
    you have to return the digits of this number within an array in reverse order.
    ex. 348597 => [7,9,5,8,4,3]
    """
    array_list = list(int(x) for x in str(n))
    return array_list[::-1] #reverse


def digitize(n):
    """
    Best solution from codewars
    """
    return map(int, str(n)[::-1])


def digitize(n):
    """
    Other solution from codewars
    """
    return [int(x) for x in str(n)[::-1]]
    
digitize(35231), # [1,3,2,5,3]