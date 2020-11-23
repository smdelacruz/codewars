def first_non_consecutive(arr):
    """Unfinished"""
    for i in range(len(arr)):
        # print(arr[i+1])
        # print(arr[-1])
        return arr[i+1] if arr[i+1] - arr[i] != 1 else "None"
        # if arr[i+1] - arr[i] != 1:
        #     print(arr[i+1])
        #     break
        # else:
        #     print("None")


# first_non_consecutive([1, 2, 3, 4, 6, 7, 8])
first_non_consecutive([31,32])
# first_non_consecutive([-3,-2,0,1])
# first_non_consecutive([4,5,6,7,8,9,11])