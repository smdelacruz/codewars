def derive(coefficient, exponent):
    """
    My solution
    Your function should multiply the two numbers, and then subtract 1 from the exponent.
    Then, it has to print out an expression (like 28x^7). "^1" should not be truncated when exponent = 2.
    derive(7, 8) --> this should output "56x^7"
    derive(5, 9) --> this should output "45x^8
    """
    return "{}x^{}".format(coefficient*exponent, exponent-1)



derive(7,8) #"56x^7"