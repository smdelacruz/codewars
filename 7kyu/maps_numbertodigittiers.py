"""
Create a function that takes a number and returns an array of strings containing the number cut off at each digit.

Examples
420 should return ["4", "42", "420"]
2017 should return ["2", "20", "201", "2017"]
2010 should return ["2", "20", "201", "2010"]
4020 should return ["4", "40", "402", "4020"]
80200 should return ["8", "80", "802", "8020", "80200"]
PS: The input is guaranteed to be an integer in the range [0, 1000000]
"""

def create_array_of_tiers(n):
    """
    My Solution
    """
    p = []
    s = ''
    for i in str(n):
        p.append(s+i)
        s += i
    return p

def create_array_of_tiers(n):
    """
    Best practices
    """
    n=str(n)
    return [n[:i] for i in range(1,len(n)+1)]

print(create_array_of_tiers(420)) #["4", "42", "420"]
print(create_array_of_tiers(2017)) #["2", "20", "201", "2017"]
print(create_array_of_tiers(4020)) # ["4", "40", "402", "4020"]
print(create_array_of_tiers(80200)) #["8", "80", "802", "8020", "80200"]