"""
Move every letter in the provided string forward 10 letters through the alphabet.

If it goes past 'z', start again at 'a'.

Input will be a string with length > 0.
abcdefghijklmnopqrstuvwxyz
"""
def move_ten(st):
    """
    My solution
    """
    new_st = []
    for x in [ord(c) for c in st]:
        alpha_10 = x + 10
        if alpha_10 > 122:
            new_st.append(96 + (alpha_10 - 122))
        else:
            new_st.append(alpha_10)
    return "".join([chr(i) for i in new_st])
print(move_ten("testcase")) #"docdmkco"
print(move_ten("returnofthespacecamel")) #"bodebxypdroczkmomkwov"