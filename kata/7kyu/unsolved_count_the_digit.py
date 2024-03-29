"""
Unsolved
Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.

Square all numbers k (0 <= k <= n) between 0 and n.

Count the numbers of digits d used in the writing of all the k**2.

Call nb_dig (or nbDig or ...) the function taking n and d as parameters and returning this count.

Examples:
n = 10, d = 1
the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.

nb_dig(25, 1) returns 11 since
the k*k that contain the digit 1 are:
1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
So there are 11 digits 1 for the squares of numbers between 0 and 25.
Note that 121 has twice the digit 1.
"""

def nb_dig(n, d):
    """
    Best practices in Kata
    """
    for i in range(n+1):
        pp = str(i * i).count(str(d))
        print(pp)
    return sum(pp)
    # return sum(str(i*i).count(str(d)) for i in range(n+1))


# print(nb_dig(25, 1))# 11)
# print(nb_dig(10, 1))# 11)
# print(nb_dig(5750, 0))# 4700)
# print(nb_dig(11011, 2))#, 9481)
# print(nb_dig(12224, 8))#, 7733)
print(nb_dig(11549, 1))#, 11905)