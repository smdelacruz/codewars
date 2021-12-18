def valid_parenthesis(string):
    """
    solution of other coderwars
    """
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        # if cnt < 0: return False
    return True if cnt == 0 else False

print(valid_parenthesis("())("))