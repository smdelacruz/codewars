"""
A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be isBeautifulString(inputString) = true.

This string contains 3 as, 3 bs, 1 c, 1 d, 1 e, and 1 f (and 0 of every other letter), so since there aren't any letters that appear more frequently than the previous letter, this string qualifies as beautiful.

For inputString = "aabbb", the output should be isBeautifulString(inputString) = false.

Since there are more bs than as, this string is not beautiful.

For inputString = "bbc", the output should be isBeautifulString(inputString) = false.

Although there are more bs than cs, this string is not beautiful because there are no as, so therefore there are more bs than as.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string of lowercase English letters.

[output] boolean

Return true if the string is beautiful, false otherwise.
"""

def isBeautifulString(inputString):
    counter = {}
    compareTo = "isBeautifulString"
    for i in compareTo:
        if i not in counter:
            counter[i] = 1
        else: counter[i] += 1
    print(counter)
    
    for x in inputString:
        

print(isBeautifulString("bbbaacdafe"))