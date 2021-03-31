"""
Task
Given a string str, reverse it omitting all non-alphabetic characters.
Example
For str = "krishan", the output should be "nahsirk".
For str = "ultr53o?n", the output should be "nortlu".
Input/Output
[input] string str
A string consists of lowercase latin letters, digits and symbols.
[output] a string
"""


def reverse_letter(string):
    return "".join([i for i in string[::-1] if i.isalpha()])



print(reverse_letter("krishan")) #"nahsirk"
print(reverse_letter("ultr53o?n")) #"nortlu"
print(reverse_letter("ab34c?n")) #"cba"
