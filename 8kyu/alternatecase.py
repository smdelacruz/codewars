def to_alternating_case(s):
    arr = []
    for i in range(len(s)):
        if s[i].isupper():
            arr.append(s[i].lower())
        else: 
            s[i].upper()
            arr.append(s[i].upper())
    return (''.join(arr))


def to_alternating_case(s):
    """
    Best Practice solution from codewars
    """
    return s.swapcase()

def to_alternating_case(s):
    """
    Other solution from codewars
    """
    return ''.join([c.upper() if c.islower() else c.lower() for c in s])
to_alternating_case("hello WORLD")