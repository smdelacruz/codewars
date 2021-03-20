import time
def are_reverses(string_1, string_2):
    """
    My solution
    """
    start = time.time()
    p = string_1 == string_2[::-1]
    print(time.time() - start)
    return p

def are_reverses(string_1, string_2):
    """
    CS Dojo solution using for loop
    """
    start = time.time()
    for i in range(len(string_1)):
        print("the i", i)
        i_2 = len(string_2) - i - 1 #will return the last in array
        print("i_2", i_2)
        if string_1[i] != string_2[i_2]:
            print(time.time() - start)
            return False
    print(time.time() - start)
    return True



print(are_reverses("ABCD", "DCBA")) #True
# print(are_reverses("ABC", "AAA")) #False