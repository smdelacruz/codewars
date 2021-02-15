"""
Given a string, turn each character into its ASCII character code and 
join them together to create a number - let's call this number total1:
'ABC' --> 'A' = 65, 'B' = 66, 'C' = 67 --> 656667
Then replace any incidence of the number 7 with the number 1, 
and call this number 'total2':

total1 = 656667
              ^
total2 = 656661
              ^
Then return the difference between the sum of the digits in total1 and total2:

  (6 + 5 + 6 + 6 + 6 + 7)
- (6 + 5 + 6 + 6 + 6 + 1)
-------------------------
                       6
"""
# def calc(x):
#     """
#     My solution - failed
#     calc('dCEpBuRpGhYyM') exp: 30 :my 138
#     """
#     total1 = sum(ord(i) for i in x)
#     total2 = []
#     for i in x:
#         ascii_str = str(ord(i))
#         if '7' in str(ascii_str):
#             ascii_str = ascii_str.replace('7', '1')
#         total2.append(int(ascii_str))
#     return total1 - sum(total2)


def calc(s):
    """
    Best practices
    """
    total1 = ''.join(map(lambda c: str(ord(c)), s))
    print(total1)
    total2 = total1.replace('7', '1')
    return sum(map(int, total1)) - sum(map(int, total2))


calc('dCEpBuRpGhYyM')# 30
calc('jaam')# 12