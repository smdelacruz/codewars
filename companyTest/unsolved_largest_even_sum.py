def solution(arr, k):
    even = []
    odd = []
    for x in arr:
        if x % 2 == 0:
            even.append(x)
        else: odd.append(x)
    sort_even = sorted(even, reverse=True)
    sort_odd = sorted(odd, reverse=True)
    print(sort_even)
    print(sort_odd)
    start = 0
    if len(sort_even) > k:
        for i in range(len(sort_even)):
            print("inside whiel")
            thesum = sum(sort_even[start:k])
            if thesum % 2 == 0:
                print(thesum)
                return thesum
            else:
                start +=1
    else:
        ppp = 1
        get_odd = 0
        while ppp != k:
            ppp = len(sort_even)
            ppp += (sort_odd[get_odd])


# print(solution([4,9,8,2,6], 3)) #18
print(solution([5,6,3,4,2], 5)) #20