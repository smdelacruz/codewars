"""
You will be given a string with sets of characters seperated by spaces (i.e. words).

Looking at the first letter of each word (case insensitive-"A" and "a" should be treated the same), you need to determine whether it falls into the positive/first half of the alphabet ("a"-"m") or the negative/second half ("n"-"z").

Return True if there are more (or equal) positive words than negative words, False otherwise.

"A big brown fox caught a bad rabbit" => True
"Xylophones can obtain Xenon." => False
"""

import unittest
def connotation(strng):
    """
    My solution
    """
    positive = "abcdefghijklm"
    words = strng.split()
    return sum([1 for i in words if i.lower()[0] in positive]) >= (len(words) / 2)


def connotation(s):
    """
    Best practices
    """
    lst = s.upper().split()
    return sum('A'<=w[0]<='M' for w in lst) >= len(lst)/2



    
print(connotation('A big brown fox caught a bad bunny'))
print(connotation('Xylophones can obtain Xenon.'))
print(connotation('CHOCOLATE MAKES A GREAT SNACK'))
print(connotation('Cranberries and newly obtained salted caramel tastes wonderful.')) #False
class Test_connotation(unittest.TestCase):
    def test_results(self):
        self.assertEqual(connotation('A big brown fox caught a bad bunny'),True)
        self.assertEqual(connotation('Xylophones can obtain Xenon.'),False)
        self.assertEqual(connotation('CHOCOLATE MAKES A GREAT SNACK'),True)
        self.assertEqual(connotation('All FOoD tAsTEs NIcE for someONe'),True)
        self.assertEqual(connotation('Is  this the  best  Kata?'),True)
