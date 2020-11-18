def abbrev_name(name):
    """
    My solution
    Pythonic way :)
    The output should be two capital letters with a dot separating them.
    It should look like this:
    Sam Harris => S.H
    Patrick Feeney => P.F
    """
    return '.'.join(c[0] for c in name.split(' ')).upper()



abbrev_name("Sam Harris") # "S.H"
abbrev_name("taylor swift") # "T.S"