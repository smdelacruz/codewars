def secondLargestFunc(arr):
    """
    the correct solution
    """
    largest = None
    secondLargest = None
    for i in arr:
        if largest==None:
            largest= i
        elif i > largest:
            secondLargest = largest
            largest = i
        # elif secondLargest == None:
        #     secondLargest = i
        elif i > secondLargest:
            secondLargest = i
    return secondLargest


print(secondLargestFunc([2,2,1]))
print(secondLargestFunc([]))
print(secondLargestFunc([5,1,2,4]))
print(secondLargestFunc([-2,-1]))
# print(secondLargest[])
