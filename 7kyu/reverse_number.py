"""
Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)

Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

Examples
 123 ->  321
-456 -> -654
1000 ->    1
"""
def reverse_number(n):
    """
    My Solution
    """
    reverse = str(abs(n))[::-1]
    return int(reverse) if n > 0 else int("-" + reverse)



print(reverse_number(123))# , 321
print(reverse_number(1000))# , 1
print(reverse_number(-123)) #, -321, 'Negative Numbers should be preserved'