def anagram(input1, input2):
    return sorted(input1) == sorted(input2)


print(anagram("hello", "hi"))
print(anagram("hello", "el"))
print(anagram("hello", "helllo"))
print(anagram("hello", "ll"))
print(anagram("hello", "lllll"))
