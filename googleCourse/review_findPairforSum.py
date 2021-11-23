def findSum(arr, num):
    pairs = []
    for i in range(len(arr)):
        print("i-", i)
        print("value-", arr[i])
        if i < len(arr):
            if (arr[i] + arr[i+1]) == 8:
                pairs.append(arr[i], arr[i+1])
    return pairs


print(findSum([1,2,3,9], 8))