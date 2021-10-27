"""
Task
You've just moved into a perfectly straight street with exactly n identical houses on either side of the road. 
Naturally, you would like to find out the house number of the people on the other side of the street. 
The street looks something like this:
Street
1|   |6
3|   |4
5|   |2
Evens increase on the right; odds decrease on the left. H
ouse numbers start at 1 and increase without gaps. 
When n = 3, 1 is opposite 6, 3 opposite 4, and 5 opposite 2.
Example
Given your house number address and length of street n, 
give the house number on the opposite side of the street.
over_the_road(address, n)
over_the_road(1, 3) = 6
over_the_road(3, 3) = 4
over_the_road(2, 3) = 5
over_the_road(3, 5) = 8
"""

def over_the_road(address, n):
    """
    My solution
    """
    odd = [x for x in n]

    counter = 1
    odd = []
    even = []
    while len(even) != n:
        if counter %2 != 0:
            odd.append(counter)
        else: even.append( counter)
        counter +=1
    if n % 2 == 0:
        find_index = even.index(n)
        oppo = odd[find_index]
    else: 
        find_index = odd.index(n)
        oppo = even[find_index]
    return oppo
    

def over_the_road(address, n):
    '''
    Input: address (int, your house number), n (int, length of road in houses) 
    Returns: int, number of the house across from your house. 
    '''
    # this is as much a math problem as a coding one 
    # if your house is [even/odd], the opposite house will be [odd/even] 
    # highest number on street is 2n 
    # Left side houses are [1, 3, ... 2n-3, 2n-1] 
    # Right side houses are [2n, 2n-2, ... 4, 2] 
    # Sum of opposite house numbers will always be 2n+1 
    return (2*n + 1 - address) 

# print(over_the_road(1, 3))# 6
print(over_the_road(3, 3))# 4