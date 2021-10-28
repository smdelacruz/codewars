def summation(num):
    """
    My solution
    Write a program that finds the summation of every number from 1 to num.
    The number will always be a positive integer greater than 0.
    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36
    :param num: 8
    :return: 36
    """
    p = []
    for i in range(num):
        p.append(i+1)
    return sum(p)


def summation(num):
    """Other solution on codewars
    range: will return sequence start from 0 to num
    """
    return sum(range(num + 1))

summation(8)