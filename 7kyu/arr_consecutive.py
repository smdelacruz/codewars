def consecutive(arr):
    """
    Create the function consecutive(arr) that takes an array of integers and
    return the minimum number of integers needed to make the contents of arr consecutive from
    the lowest number to the highest number.

    For example:
    If arr contains [4, 8, 6] then the output should be 2 because two numbers need to be added to the array (5 and 7)
    to make it a consecutive array of numbers from 4 to 8. Numbers in arr will be unique.
    """
    if arr:
        sorted_arr = sorted(arr)
        complete_values = [i for i in range(sorted_arr[0], sorted_arr[-1])]
        missing_val = [x for x in list(set(arr + complete_values)) if x not in sorted_arr]
        return len(missing_val)
    else: return 0

def consecutive(arr):
    """
    Best solution on codewars
    """
    return max(arr) - min(arr) + 1 - len(arr) if arr else 0



consecutive([4, 8, 6])  # 2
# consecutive([]) #0