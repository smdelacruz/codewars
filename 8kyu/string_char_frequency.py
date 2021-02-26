"""
Description

Welcome, Warrior! In this kata, you will get a message and you will need to get the frequency of each 
and every character!

Explanation

Your function will be called char_freq/charFreq/CharFreq and you will get passed a string, 
you will then return a dictionary (object in JavaScript) with as keys the characters, 
and as values how many times that character is in the string. 
You can assume you will be given valid input.

"""


def char_freq(message):
    """
    My Solution
    """
    p = {}
    counter = 1

    for i in message:
        p[i] = counter if i not in p else p[i] + 1
    return p

# best solution
from collections import Counter

def char_freq(message):
    return Counter(message)


print(char_freq("I like cats")) # {'a': 1, ' ': 2, 'c': 1, 'e': 1, 'I': 1, 'k': 1, 'l': 1, 'i': 1, 's': 1, 't': 1}