"""
write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.

the string should start with a 1.

a string with size 6 should return :'101010'.

with size 4 should return : '1010'.

with size 12 should return : '101010101010'.

The size will always be positive and will only use whole numbers.
"""

def stringy(size):
    """
    My solution
    """
    p = ''
    for i in range(1, size+1):
        if i % 2 != 0:
            p += '1'
        else: p += '0' #print('0')
    return p


def stringy(size):
    """Best solution solution for me """
    return "".join([str(i % 2) for i in range(1, size + 1)])

print((stringy(3)))
print((stringy(5))) #'10101',
print((stringy(12))) #'101010101010',
print((stringy(26))) #'10101010101010101010101010',
print((stringy(28))) #'1010101010101010101010101010',