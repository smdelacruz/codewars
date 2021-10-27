"""
Your task is to write a function called valid_spacing() or validSpacing() which checks if a string has valid spacing. The function should return either True or False.

For this kata, the definition of valid spacing is one space between words, and no leading or trailing spaces. Below are some examples of what the function should return.

'Hello world' = True
' Hello world' = False
'Hello world  ' = False
'Hello  world' = False
'Hello' = True
# Even though there are no spaces, it is still valid because none are needed
'Helloworld' = True 
# True because we are not checking for the validity of words.
'Helloworld ' = False
' ' = False
'' = True
Note - there will be no punctuation or digits in the input string, only letters.
"""
import unittest

def valid_spacing(s):
    """
    My solution
    """
    split_word = s.split(" ")
    word = [i for i in split_word if i.isalnum()]
    return " ".join(word) == s

def valid_spacing(s):
    """
    Best solution
    """
    return s == ' '.join(s.split())

print(valid_spacing('Hello   world'))

# class Test_valid_spacing(unittest.TestCase):
#     def test_results(self):
#         self.assertEqual(valid_spacing('Hello world'),True)
#         self.assertEqual(valid_spacing(' Hello world'),False)
#         self.assertEqual(valid_spacing('Hello  world '),False)
#         self.assertEqual(valid_spacing('Hello'),True)
#         self.assertEqual(valid_spacing('Helloworld'),True)


