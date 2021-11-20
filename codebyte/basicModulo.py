

"""
convert minutes to hours
inputs:
-negative
-0
-string ? 
less than 60
"""

def minToHr(min):
    return "{} hr and {} min".format(( min / 60), (min % 60))

print(minToHr(63))
print(minToHr(0))
print(minToHr(-0))
print(minToHr(45))