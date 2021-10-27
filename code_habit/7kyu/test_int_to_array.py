"""
Write a function that accepts two arguments and generates a sequence containing the integers from the first argument to the second inclusive.

Input
Pair of integers greater than or equal to 0. The second argument will always be greater than or equal to the first.

Example
generate_integers(2, 5) # --> [2, 3, 4, 5]

"""


def generate_integers(m, n):
    return list(range(m, n+1))

def test_generate_integers():
    assert generate_integers(0,0) == [0]
    assert generate_integers(2,5) == [2,3,4,5]
    assert generate_integers(2,10) == [2, 3, 4, 5, 6, 7, 8, 9, 10]