"""
Description:
Move all exclamation marks to the end of the sentence

Examples
remove("Hi!") === "Hi!"
remove("Hi! Hi!") === "Hi Hi!!"
remove("Hi! Hi! Hi!") === "Hi Hi Hi!!!"
remove("Hi! !Hi Hi!") === "Hi Hi Hi!!!"
remove("Hi! Hi!! Hi!") === "Hi Hi Hi!!!!"
"""

def remove(s):
    exclamation_count = s.count("!")
    new_word = s.replace("!", "")
    for a in range(exclamation_count):
        new_word += "!"
    return new_word


""""
Other Codewarrior solution - simplified
def remove(s):
    return s.replace('!','') + s.count('!') * '!'
"""


def test_remove():
    tests = [
    ["Hi!", "Hi!"],
    ["Hi! Hi!", "Hi Hi!!"],
    ["Hi! Hi! Hi!" , "Hi Hi Hi!!!"],
    ["Hi! !Hi Hi!", "Hi Hi Hi!!!"],
    ["Hi! Hi!! Hi!" , "Hi Hi Hi!!!!"],
    ]

    for input, expected in tests:
        assert remove(input)== expected