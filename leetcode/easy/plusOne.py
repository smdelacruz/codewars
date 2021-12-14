
# def plusOne(digits):
#     """
#     my not owrking solution
#     """
#     new_digit = (digits[-1] + 1)
#     if len(str(new_digit)) > 1:
#         digits.pop()
#         for i in str(new_digit):
#             digits.append(int(i))
#     else: digits[-1] += 1
#     return digits

def plusOne(digits):
    print(map(str, digits))
    number = str(int(''.join(map(str, digits)))+1)
    #First, join all the numbers toguether into one string, by using map to turn all ints into strings, then joining them all with join()
    #Then, turn our string into an integer (ex: 123) and add +1 to it
    #Finally, turn it back into a string, and use list() to turn it into an array.
    digits = list(number)
    return digits
print(plusOne([9]))
print(plusOne([1,2,9]))