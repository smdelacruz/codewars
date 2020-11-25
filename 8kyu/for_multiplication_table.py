def multi_table(number):
    """
    My solution
    multiplication table
    return :
        1 * 5 = 5
        2 * 5 = 10
        3 * 5 = 15
        4 * 5 = 20
        5 * 5 = 25
        6 * 5 = 30
        7 * 5 = 35
        8 * 5 = 40
        9 * 5 = 45
        10 * 5 = 50
    """
    return "\n".join("{} * {} = {}".format(p, number, p*number) for p in range(1,11))

multi_table(5)