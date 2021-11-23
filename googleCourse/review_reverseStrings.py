def reverse(string_1, string_2):
    """
    the correct solution
    """
    for i in range(len(string_1)):
        i_2 = len(string_2) - i - 1 #AWESOME
        if string_1[i] != string_2[i_2]:
            return False
    return True


print(reverse("ABC", "CBA"))
print(reverse("ABC", "ABA"))

