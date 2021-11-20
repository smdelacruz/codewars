def two_highest(arg1):
    ss = set(arg1)
    ll = list(set(arg1))
    print(sorted(list(set(arg1)), reverse=True))[:2]
    print(sorted(set(arg1), reverse=True))[:2]
print(two_highest([15, 20, 20, 20,20, 19, 17]))