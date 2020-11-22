def sum_str(a, b):
    """
    Unlocked solution: Best solution
    Create a function that takes 2 positive 
    integers in form of a string as an input, and outputs the sum (also as a string):
    ex. sumStr("4", "5")    // should output "9"
    sumStr("34", "5")   // should output "39"
    """
    return str(int(a or 0) + int(b or 0))


sum_str("4","5")# "9"
sum_str("4","")# "0"