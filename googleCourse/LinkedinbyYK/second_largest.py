# def second_largest(arr):
#     """
#     My solution using built in functions
#     """
#     if arr:
#         return sorted(arr, reverse=True)[1]
#     else: return None

def second_largest(arr):
    """
    my solution using for loop
    """
    largest = None
    second_largest = None

    for current_number in arr:
        if largest == None:
            largest = current_number
        elif largest <= current_number:
            second_largest = largest
            largest = current_number
    return second_largest
            

print(second_largest([1,3,4,5,0,2]))
print(second_largest([1,2,2]))
print(second_largest([]))
print(second_largest([2]))
print(second_largest([-2, -1]))
print(second_largest([5,1,2,4]))
