"""
You probably know that some characters written on a piece of paper, after turning this sheet 180 degrees, can be read, although sometimes in a different way. So, uppercase letters "H", "I", "N", "O", "S", "X", "Z" after rotation are not changed, the letter "M" becomes a "W", and Vice versa, the letter "W" becomes a "M".

We will call a word "shifter" if it consists only of letters "H", "I", "N", "O", "S", "X", "Z", "M" and "W". After turning the sheet, this word can also be read, although in a different way. So, the word "WOW "turns into the word "MOM". On the other hand, the word "HOME" is not a shifter.

Find the number of unique shifter words in the input string (without duplicates). All shifters to be counted, even if they are paired (like "MOM" and "WOW"). String contains only uppercase letters.

Examples

shifter("SOS IN THE HOME") == 2 # shifter words are "SOS" and "IN"
shifter("WHO IS SHIFTER AND WHO IS NO") == 3 # shifter words are "WHO", "IS", "NO"
shifter("TASK") == 0 # no shifter words
shifter("") == 0 # no shifter words in empty string
"""

def shifter(st): 
    """
    Unresolved. Use unlock solution
    """
    shifters_char = ["H", "I", "N", "O", "S", "X", "Z"]
    chars = st.split(" ")
    p = []
    counter = 1
    for char in st:
        print("char", char)
        for s in shifters_char:
            if char == s:
                counter =+1
                p.append(counter) if coun
            elif char == " ":
                counter = 0  
    
    print("".join(p))
    # for i in shifters_char:
    #     for x in chars:
    #         if i in x:
    #             temp += 
    #             p.append(str(x))
    # return len(set(p))

print(shifter("ON"))#1
print(shifter("JS"))#0
print(shifter("I III I III"))# 2)
# print(shifter("OS IS UPDATED")) # 2





def shifter(st): 
    """
    Clever solution from other code warriors
    """
    return sum(all(elem in "HIMNOSWXZ" for elem in x) for x in set(st.split()))