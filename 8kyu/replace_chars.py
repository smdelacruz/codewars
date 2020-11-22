def correct(thestring):
    misinterpret = {
        '5' : 'S',
        '0' : 'O',
        '1' : 'I'
    }
    # hello = (thestring.replace(a) for a in thestring)
    # hello = [misinterpret[c] for c in thestring if misinterpret[c]]
    # for i in thestring:
    #     print(i)
    #     p = misinterpret.get(i)
    #     print(p)
    #     if p:
    #         i.replace(p)
    #     print(p)
    hello = (thestring.replace(misinterpret[c] for c in thestring, ))
    print(hello)

correct("L0ND0N")