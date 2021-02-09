def odds(values):
    """
    Time to test your basic knowledge in functions! 
    Return the odds from a list:
    odds([1,2,3,4,5]) #=> [1,3,5]
    """
    return [a for a in values if a % 2 == 1]


def odds(values):
    """
    Best solution from other code warriors
    """
    return [i for i in values if i%2]