import math
def sockMerchant(n, ar):
    """
    my solution
    """
    unique_socks = list(set(ar))
    num_of_pairs = 0
    for i in unique_socks:
        num_of_pairs += (ar.count(i) / 2)
    return num_of_pairs

# def sockMerchant(n, ar):
#     """Optimized solution"""
#     return sum([ar.count(i)//2 for i in set(ar)])

print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])) # 3