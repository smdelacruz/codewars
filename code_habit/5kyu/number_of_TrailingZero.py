import math
import time 
def zeros(n):
    """
    my solution , timedout
    """
    if n == 0: return 0
    factorial = math.factorial(n)
    zero_counter = 0

    start = time.clock()
    factorial_reversed = str(factorial)[::-1]
    for j in factorial_reversed:
        if j != "0":
            break
        zero_counter += 1
    # end = time.localtime()
    print(time.clock() - start)
    return zero_counter

print(zeros(6))#1
print(zeros(12))#2