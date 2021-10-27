def square_sum(numbers):
    """
    Complete the square sum function so that it squares each number passed into it and then sums the results together.
    For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9
    """
    squared = []
    for i in numbers:
        squared.append(i**2)
    return sum(squared)


def square_sum(numbers):
    """
    Best solution from codewars
    """
    return sum(x ** 2 for x in numbers)


square_sum([0, 3, 4, 5]) #5