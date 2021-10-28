"""
Create function that takes one positive three digit integer and rearranges its 
digits to get maximum possible number. Assume that argument is integer. 

Return null (nil for ruby) if argument is not valid.

maxRedigit(123); // returns 321
"""


def max_redigit(num): 
    listing = [i for i in str(num)]
    return None if len(listing) != 3 or num > 0 else "".join(sorted(listing, reverse=True)) 


print(max_redigit(123)) #, 321)
print(max_redigit(555)) #, 555)
print(max_redigit(1000)) #, None)