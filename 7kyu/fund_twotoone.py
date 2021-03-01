"""
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""


def longest(a1, a2):
    """
    My solution
    """
    a = a1 + a2
    return "".join(sorted(list(set([i for i in a]))))


def longest(a1, a2):
    """
    Bes practices
    """
    return "".join(sorted(set(a1 + a2)))



print(longest("aretheyhere", "yestheyarehere")) # aehrsty
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding")) # abcdefghilnoprstu
print(longest("inmanylanguages", "theresapairoffunctions")) # acefghilmnoprstuy