"""
Given n , range 1 to n print:
if i is a mltiple of both 3 and 5, print FizzBuzz
if i is a multiple of only 3, Fizz
if i is a multiple of only 5, Buzz
if i is not a multiple of 3 or 5, print value of i
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    for i in range(1,n+1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif((i % 3)) == 0:
            print("Fizz")
        elif((i % 5)) == 0:
            print("Buzz")
        else: print(i)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
