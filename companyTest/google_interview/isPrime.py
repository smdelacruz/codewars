def isPrime(num):
    if num <= 1: return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


def largestPrime(nlist):
    temp = 0
    for i in nlist:
        if isPrime(i):
            if i > temp:
                temp = i
    return temp
print(largestPrime([2,3,4,5,6,7]))
print(largestPrime([2,3,4,5,7,6,13,5]))