"""
Please write a function that sums a list, but ignores any duplicate items in the list.

For instance, for the list [3, 4, 3, 6] , the function should return 10.
"""

def sum_no_duplicates(l):
    """
    My solution: sucks!!! 
    """
    print(l.count)
    no_duplicate = []
    duplicated = []
    for i in l:
        if i not in no_duplicate and i not in duplicated:
            no_duplicate.append(i)
        elif i in duplicated and i not in no_duplicate:
            pass
        else:
            no_duplicate.remove(i)
            duplicated.append(i)
    return sum(no_duplicate)



# def sum_no_duplicates(l):
#     """
#     Best solution by other code warriors
#     """

#     return sum(n for n in set(l) if l.count(n) == 1)


# print(sum_no_duplicates([1, 1, 2, 3]))#  5)
# print(sum_no_duplicates([0, 10, 8, 9, 7, 3, 3, 9, 3, 6, 0]))#  21
print(sum_no_duplicates([5, 6, 10, 3, 10, 10, 6, 7, 0, 9, 1, 1, 6, 3, 1]))#, 21))