# Modify the following function:
def appears_twice(given_list):
    """
    My solution
    """
    name = {}
    counter = 0
    for i in given_list:
        if i in name: 
            return i
        name[i] = counter
    return ""

print(appears_twice(['George', 'Tom', 'Emily', 'Jenny', 'Tom']))