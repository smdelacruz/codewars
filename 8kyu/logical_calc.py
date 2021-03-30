"""
Given an array of Boolean values and a logical operator, 
return a Boolean result based on sequentially applying the operator to the values in the array.

Examples

booleans = [True, True, False], operator = "AND"
True AND True -> True
True AND False -> False
return False
booleans = [True, True, False], operator = "OR"
True OR True -> True
True OR False -> True
return True
booleans = [True, True, False], operator = "XOR"
True XOR True -> False
False XOR False -> False
return False
Input

an array of Boolean values (1 <= array_length <= 50)
a string specifying a logical operator: "AND", "OR", "XOR"
"""


def logical_calc(array, op):
    p = {"AND":'=', "OR": "|", "XOR": "^"}
    count = range(len(array))
    first_two = False
    if op == "AND":
        first_two =  array[0] == array[1]
    elif op == "OR":
        first_two =  array[0] | array[1]
    elif op == "XOR":
        first_two =  array[0] ^ array[1]

    if count > 2:
        for a in range(2,len(array)):
            if op == "AND":
                first_two == array[a]
            elif op == "OR":
                first_two =  array[a]
            elif op == "XOR":
                first_two =  array[a]
        return first_two
    # for a in range(len(array)):
    #     if count > 2:
    #     result = array[a] + p[op] + array[a+1]


print(logical_calc([True, False], "AND"))
print(logical_calc([True, False], "OR"))
print(logical_calc([True, False], "XOR"))
print(logical_calc([True, False, False], "AND"))
print(logical_calc([True, False, False], "OR"))....
print(logical_calc([True, False, False], "XOR"))