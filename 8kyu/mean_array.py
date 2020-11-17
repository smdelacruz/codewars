import math


def get_average(marks):
    """
    Return the average of the given array rounded down to its nearest integer.
    :param marks: array ex [1, 5, 87, 45, 8, 8]
    :return: 25
    """
    sum_of_all = sum(marks)
    return math.floor(sum_of_all / len(marks))
