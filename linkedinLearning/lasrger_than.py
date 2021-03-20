# Input:
#  a: The first non-negative integer in string. Example: "123"
#  b: The second non-negative integer in string. Example: "3344"
# Returns:
#  True if a is larger than b.
#  False if a is smaller than or equal to b.
# NOTE! Cannot use converter int()
import time
def larger_than(a, b):
    """
    My solution
    """
    start = time.time()
    a_len = len(a)
    b_len = len(b)
    if a_len < b_len:
        print(time.time() - start)
        return False
    elif a_len > b_len:
        print(time.time() - start)
        return True
    elif a_len == b_len:
        for i in range(a_len):
            if a[i] > b[i]:
                print(time.time() - start)
                return True
        return False


print(larger_than( "112", "111" )) #True
print(larger_than( "525", "1111" )) #False
print(larger_than( "1", "1" )) #False