# def secondLargest(s):
#     """
#     My solution using buil-in functions
#     """
#     return sorted(s, reverse=True)[1] if len(s) > 1 else None

def secondLargest(s):
    """
    CS Dojo Solution
    """
    largest = None
    second_largest = None
    for number in s:
        if largest == None:
            largest = number
        elif number > largest:
            second_largest = largest
            largest = number
        elif second_largest == None:
            second_largest = number
        elif number > second_largest:
            second_largest = number
    return second_largest




print(secondLargest([1,5,2,0,3,4])) #4
print(secondLargest([2,2,1])) #2
print(secondLargest([])) #None
print(secondLargest([4])) #None



