# Input: A list / array with integers.  For example:
# [3, 4, 1, 2, 9]
# Returns:
#  Nothing. However, this function will print out
#  a pair of numbers that adds up to 10. For example,
#  1, 9.  If no such pair is found, it should print
#  "There is no pair that adds up to 10.".
def pair10(given_list):

    for i in given_list:
        find_num = 10 - i
        if find_num in given_list:
            return "{}, {}".format(int(i), int(find_num))
    return "There is no pair that adds up to 10."


print(pair10([3, 4, 1, 2, 9]))
print(pair10([0,10]))
print(pair10([10]))
print(pair10([-11, -20, 2, 4, 30]))