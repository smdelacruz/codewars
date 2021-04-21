"""
Your task is to find the number couple with the greatest difference from a given array of number-couples.

All number couples will be given as strings and all numbers in them will be positive integers.

For instance: ['56-23','1-100']; in this case, you should identify '1-100' as the number couple with the
greatest difference and return it.

In case there are more than one option, for instance ['1-3','5-7','2-3'], you should identify whichever is first,
so in this case '1-3'.

If there is no difference, like so ['11-11', '344-344'], return false.
"""

def diff(arr):
    """
    My ugly solution
    """
    highest = 0
    holder = 0
    for i in arr:
        n = i.split("-")
        print(n)
        diff = abs(int(n[0]) - int(n[1]))
        print(diff)
        if diff > highest:
            highest = diff
            holder = i
        elif diff == 0 and diff > highest:
            holder = 0
    return holder if holder != 0 else False


def diff(arr):
    """Best Practices"""
    r = arr and max(arr, key = lambda x : abs(eval(x)))
    return bool(arr and eval(r)) and r



print(diff(['1-2','2-4','5-7','8-9','44-45'])) # 2-4
print(diff(['43-45', '1021-55', '000-18888', '92-34', '76-32', '99-1', '1020-54'])) # '000-18888'
print(diff(['45896-2354','4654-556767','2455-423522','3455-355','34-34','2524522-0'])) # '2524522-0'
print(diff(['33-33', '77-77'])) #, False