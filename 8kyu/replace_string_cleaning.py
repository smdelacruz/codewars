def string_clean(s):
    """
    My solution
    Function will return the cleaned string
    """
    for i in ["1","2","3","4","5","6","7","8","9","0"]:
        s = s.replace(i, "")
    return s



def string_clean(s):
    """
    BEst practice solution from other code warriors
    """
    return ''.join(x for x in s if not x.isdigit())
print(string_clean(""))
print(string_clean("(E3at m2e2!!)"))
print(string_clean("Dsa32 cdsc34232 csa!!! 1I 4Am cool!"))
print(string_clean("123456789"))
print(string_clean("Wh7y can't we3 bu1y the goo0d software3? #cheapskates3"))