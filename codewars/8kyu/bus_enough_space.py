"""
You have to write a function that accepts three parameters:

cap is the amount of people the bus can hold excluding the driver.
on is the number of people on the bus excluding the driver.
wait is the number of people waiting to get on to the bus excluding the driver.
If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.
"""


def enough(cap, on, wait):
    """
    My sollution
    """
    if cap > (on + wait):
        print(cap)
        print(on + wait)
        return 0
    else: return (on + wait) - cap



def enough(cap, on, wait):
    """
    Best practices
    """
    return max(0, wait - (cap - on))


print(enough(10, 5, 5))
print(enough(100, 60, 50))
print(enough(20, 5, 5))