def twoSum(nums, target):
    """
    My solution
    """
    output = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in output:
            return [output[diff], i]
        output[nums[i]] = i
    return None
            

# 4-2 = 2
# output = {2: 0, }

# 4-1 = 3
# output = {2: 0, 1: 1, 5:2}

# 4-5 = -1
# output = {2: 0, 1: 1, 5:2}

# 4-3 = 1

print(twoSum([2,1,5,3], 4))