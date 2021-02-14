def pipe_fix(nums):
    """
    #Task Given the a list of numbers, 
    # return the list so that the values increment by 1 for each index up to the maximum value.
    #Example:
    Input: 1,3,5,6,7,8
    Output: 1,2,3,4,5,6,7,8
    """

    p = sorted(nums)
    print([x for x in range(p[0],p[-1]+1)])


pipe_fix([1, 2, 3, 5, 6, 8, 9])
pipe_fix([6, 9])
pipe_fix([1, 2, 3, 12])