"""
Unsolved
Complete the function that takes an odd integer (0 < n < 1000000) 
which is the difference between two consecutive perfect squares, 
and return these squares as a string in the format "bigger-smaller"
9  -->  "25-16"
5  -->  "9-4"
7  -->  "16-9"
"""


def find_squares(n):
    """
    Best solution from kata
    Clever solution
    """
    m = (n-1)//2
    print("mmm", m)
    print("(m+1)**2", (m+1)**2)
    print("(m+1)**2", (m**2))
    # return f'{(m+1)**2}-{m**2}'
    # print("{}".format((m+1)**2-(m**2)))


print(find_squares(9))
print(find_squares(5))
print(find_squares(7))