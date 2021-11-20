def FindIntersection(strArr):
    """solution 1 --> need improvement"""
    # list1 = strArr[0].split(", ")
    # list2 = strArr[1].split(", ")
    # new_list = []
    # for i in range(max(len(list1), len(list2))):
    #     if list1[i] in list2:
    #         new_list.append(list1[i])
    # return ",".join(new_list)

    """solution 2 --> need improvement"""
    # list1 = strArr[0].split(", ")
    # list2 = strArr[1].split(", ")
    # new_list = []
    # finding = []
    # bigger = []
    # if len(list1) >= len(list2):
    #     bigger = list1 
    #     finding = list2
    # else: 
    #     bigger = list2
    #     finding = list1
    # for i in range(max(len(list1), len(list2))):
    #     if bigger[i] in finding:
    #         new_list.append(list1[i])
    # return ",".join(new_list) if new_list else False



    """"
    good solution """
    a = map(int, strArr[0].split(', '))
    b = map(int, strArr[1].split(', '))
    c = list(set(a) & set(b)) #intersection
    print(c)
    c.sort()
    return ','.join(map(str, c))

    # print(FindIntersection(input()))
    
# keep this function call here 
print(FindIntersection(["1, 2, 3, 4, 5", "6, 1, 2, 5, 10"]))