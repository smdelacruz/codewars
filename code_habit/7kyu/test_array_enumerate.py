



def incrementer(nums):
    """
    my solution
    """
    # new_nums = []
    # for i, v in enumerate(nums, 1):
    #     total = i+v
    #     if len(str(total)) >= 2:
    #         total = list(str(total))[-1]
    #     new_nums.append(int(total))
    # return new_nums

    return [int(list(str(i+v))[-1]) if len(str(i+v)) >= 2 else i + v for i,v in enumerate(nums, 1)]

"""
Other Codewarrior solution - simplified
def incrementer(nums):
    return [ (v+i)%10 for i,v in enumerate(nums,1) ]
"""

print(incrementer([1, 2, 3]))
print(incrementer([3, 6, 9, 8, 9])) #48224