def calc(x):
    print(ord(i) for i in x)
    total1 = sum(ord(i) for i in x)
    total2 = []
    for i in x:
        ascii_int = ord(i)
        ascii_str = str(ascii_int)
        if '7' in str(ascii_str):
            ascii_str = ascii_str.replace('7', '1')
        total2.append(int(ascii_str))
        print(total2)
    print(total1 - sum(total2))
    return total1 - sum(total2)

calc('dCEpBuRpGhYyM')# 30
# calc('jaam')# 12