def sum_or_product(arraylist, count):
    """
    https://www.codewars.com/kata/5c4cb8fc3cf185147a5bdd02
    This does not have python yet,
    Pushed as kata in the future
    """
    sorted_array = sorted(arraylist, reverse=True)
    print(sorted_array)
    sum_result = sum(sorted_array[i] for i in range(count))
    print(sum_result)

    last_three = [sorted_array[-i] for i in range(1, count+1)]
    print(last_three)
    temp = None
    counter = 1
    for a in range(len(last_three)):
        if counter < len(last_three):
            aa = last_three[a] if temp==None else temp
            bb = last_three[a+1]
            temp = aa * bb
            print("temp",temp) #72
        counter +=1

    if temp > sum_result:
        return "product"
    elif temp == sum_result:
        return "same"
    else:
        return "sum"
sum_or_product([10, 41, 8, 16, 20, 36, 9, 13, 20], 3)