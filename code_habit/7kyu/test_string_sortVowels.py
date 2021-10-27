"""
Sort the Vowels!
In this kata, we want to sort the vowels in a special format.

Task
Write a function which takes a input string s and return a string in the following way:

   
                  C|                          R|
                  |O                          n|
                  D|                          d|
   "CODEWARS" =>  |E       "Rnd Te5T"  =>      |
                  W|                          T|
                  |A                          |e
                  R|                          5|
                  S|                          T|

Notes:

List all the Vowels on the right side of |
List every character except Vowels on the left side of |
Return every character in its original case
Each line is seperated with \n
Invalid input ( undefined / null / integer ) should return an empty string
"""

def sort_vowels(s):
    new_word = ''
    vowels = ['a','e','i', 'o', 'u', 'A', 'E', 'U', 'I', 'O']
    if type(s) != str: return ''
    for i in s:
        if i not in vowels:
            new_word += i + "|\n"
        else: new_word += "|" + i + "\n"
    return new_word.strip()

"""
Other Codewarrior solution - simplified
def sort_vowels(s):
    try:
        return '\n'.join('|' + i  if i.lower() in 'aioue' else i + '|' for i in s)
    except:
        return ''
"""

def test_sort_vowels():
    assert sort_vowels('Codewars') == 'C|\n|o\nd|\n|e\nw|\n|a\nr|\ns|'
    assert sort_vowels('Rnd Te5T') == 'R|\nn|\nd|\n |\nT|\n|e\n5|\nT|'
    assert sort_vowels(1337) == ''