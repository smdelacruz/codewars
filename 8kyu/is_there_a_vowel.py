"""
Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).
If they are, change the array value to a string of that vowel.
Return the resulting array.
"""

def is_vow(inp):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_ascii = {}
    for i in vowels:
        vowels_ascii[i] = ord(i)
    for x in inp:
        if x in vowels_ascii.keys():



def test_is_vow():
    """
    command pytest __filename__ -v
    """
    assert is_vow([118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106 ]) == [118, "u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106 ]
    assert is_vow([100,100,116,105,117,121 ]) == [100,100,116,"i","u",121 ]