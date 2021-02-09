def nth_even(n):
    """
    My solution ; also best solution
    nthEven(1) //=> 0, the first even number is 0
    nthEven(3) //=> 4, the 3rd even number is 4 (0, 2, 4)

    nthEven(100) //=> 198
    nthEven(1298734) //=> 2597466
    """
    return n * 2 - 2
    


nth_even(1) #0
nth_even(100) #198
nth_even(3)