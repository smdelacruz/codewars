"""
Math hasn't always been your best subject, and these programming symbols always trip you up! I mean, does ** mean "Times, Times" or "To the power of"? Luckily, you can create the function to write out the expressions for you!

The operators you'll need to use are:

"+"   -->  "Plus"
"-"   -->  "Minus"
"*"   -->  "Times"
"/"   -->  "Divided By"
"**"  -->  "To The Power Of"
"="   -->  "Equals"
"!="  -->  "Does Not Equal"
Notes:

the input will always be given as a string, in the following format: number space operator space number; for example: "1 + 3" or "2 - 10"
the numbers used will be 1 to 10
the valid operators and the relevant texts are stored in the preloaded dictionary/hash OPERATORS
invalid operators will also be tested, to which you should return "That's not an operator!"
Examples
"4 ** 9"  -->  "Four To The Power Of Nine"
"10 - 5"  -->  "Ten Minus Five"
"2 = 2"   -->  "Two Equals Two"
"2 x 3"   -->  "That's not an operator!"
"""

OPERATORS = {
    "+" : "Plus",
    "-": "Minus",
    "*": "Times",
    "/": "Divided By",
    "**": "To The Power Of",
    "=": "Equals",
    "!=": "Does Not Equal",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten",
}
def expression_out(exp):
    convert = []
    for i in exp.split(" "):
        if i not in OPERATORS.keys():
            return "That's not an operator!"
        else:
            convert.append(OPERATORS[i])
    return " ".join(convert)
    # convert = [OPERATORS[i] if i in OPERATORS.keys() else "That's not an operator!" for i in p]
    # return " ".join(convert)

print(expression_out("1 + 3")) #One Plus Three
print(expression_out("2 / 2")) #One Plus Three
print(expression_out("2 $ 2")) #One Plus Three


