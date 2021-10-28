def simple_multiplication(number):
    """
    My solution
    This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
    """
    print(number)
    if number % 2 == 0:
        print(number)

        # return number * 8
        print(number * 8)
    # else: return number * 9
    else: print(number * 9)


simple_multiplication(2)