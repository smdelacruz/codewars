def century(year):
    # unFinish 
    pp = year / 100
    ll = "{:.2f}".format(pp)
    print(ll)
    p = year // 100
    print(p)
    return year % 100



print(century(1705)) #18
# print(century(1900)) #19
# print(century(89)) #1
# print(century(356)) #4