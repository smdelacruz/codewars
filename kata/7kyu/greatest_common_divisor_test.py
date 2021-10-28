"""
Find the greatest common divisor of two positive integers.
The integers can be large, so you need to find a clever solution.

The inputs x and y are always greater or equal to 1,

so the greatest common divisor will always be an integer that is also greater or equal to 1.
"""

import unittest

def mygcd(x, y):
    """
    My Solution
    """
    highest_divisor = 1
    max_num = max(x, y)
    print(max_num)
    for i in range(1, max_num):
        if x % i == 0 and y % i == 0:
            highest_divisor = i
        else: pass
    return highest_divisor


#Try to make your own gcd method without importing stuff
def mygcd(x,y):
    """Best Practice solution by other code wars"""
    while y:
        x,y=y,x%y
    return x

def mygcd(x,y):
    """Clever solution by other code wars"""
  return x if y == 0 else mygcd(y, x % y)


class TestMygcd(unittest.TestCase):
    def test_results(self):

        self.assertEqual(mygcd(30,12),6)
        self.assertEqual(mygcd(8,9),1)
        self.assertEqual(mygcd(1,1),1)


