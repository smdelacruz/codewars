def cinema(b, g):
    s = ""
    print(max(b,g))
    for i in range(max(b,g)):
        print("i", i)
        while max(b, g) != 0:
            if b > g : 
                s += "B"
                b =- 1
            else: 
                s += "G"
                g =- 1
    return s


    # for bb in range(b):
    #     s += "B"    
    #     while g != 0:
    #         s += "G"
    #         g -=1
    # return s
# print(cinema(1, 1)) #["BG", "GB"])
print(cinema(1, 2)) #["GBG", "GB"])