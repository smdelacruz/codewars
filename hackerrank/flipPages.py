#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#
"""
Given  and , find and print the minimum number of pages that must be turned in order to arrive at page .
[0,1], [2,3], [4,5] # 5pages, find 4page it will take 0 flip to find page no.4 if DESC
[0,1], [2,3], [4,5], [6,0]# 6pages, find 2page it will take 1 flip to find page no.2 if ASC
return the min number of flip if ASC or DESC
"""
def pageCount(numofpages, page):
    """
    Clever Solution from HackerRank
    """
    print(page/2)
    print(numofpages/2)
    print(numofpages/2-page/2)
    print(min(numofpages/2-page/2))

print(pageCount(6,2)) #1
# print(pageCount(5,4)) #0
# print(pageCount(5,3)) #1