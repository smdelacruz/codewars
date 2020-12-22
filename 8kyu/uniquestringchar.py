def solve(a,b):
    pp = []
    nstr = []
    for i in a:
        if i in b:
            pp.append(i)
    print(pp)
    for bb in pp:
        if bb not in a:
            nstr.append(bb)
        if bb not in b:
            nstr.append()
    return nstr





print(solve("xyab","xzca")) #,"ybzc"
print(solve("abcd","xyz"))#,"abcdxyz"