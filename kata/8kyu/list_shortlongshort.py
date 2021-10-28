def solution(a, b):
    """
    My solution
    Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the
    outside and the longer string on the inside.
    The strings will not be the same length, but they may be empty ( length 0 ).
    """
    return a + b + a if len(a) < len(b) else b + a + b


def solution(a, b):
    "Clever solution on codewars"
    return '{0}{1}{0}'.format(*sorted((a, b), key=len))



solution("1", "22") # returns "1221"
solution('False','B') # ---> Failed here