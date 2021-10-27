"""
Write a function generateIntegers/generate_integers that accepts a single argument n/$n and generates an array containing the integers from 0 to n/$n inclusive.

For example, generateIntegers(3)/generate_integers(3) should return [0, 1, 2, 3].

n/$n can be any integer greater than or equal to 0.
"""

def generate_integers(nn):
    return [a for a in range(nn+1)]

"""
Other Codewarrior solution - simplified
def generateIntegers(n):
  return list(range(n + 1))
"""

def test_generate_integers():
    assert generate_integers(0) == [0]
    assert generate_integers(3) == [0,1,2,3]
    assert generate_integers(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]