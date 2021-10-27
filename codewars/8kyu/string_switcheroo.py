"""
Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

Example:

'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb'
"""

def switcheroo(string):
    p = ''
    for i in string:
        if i == 'a': p += 'b'
        elif i == 'b': p+= 'a'
        else: p+= i
    return p


def switcheroo(s):
    """
    best practices
    maketrans: If only one parameter is specified, this has to be a dictionary describing how to perform the replace.
    If two or more parameters are specified, this parameter has to be a string specifying the characters you want to replace.

    """
    return s.translate(str.maketrans('ab','ba'))

print(switcheroo("abc")) # bac
switcheroo('aaabcccbaaa') #bbbacccabbb
switcheroo('abababababababab') # babababababababa
switcheroo('aaaaa') #bbbbb