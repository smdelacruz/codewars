"""
Write a function that takes a string and returns an array containing binary numbers equivalent to the ASCII codes of the characters of the string. The binary strings should be eight digits long.
v
Example: 'man' should return [ '01101101', '01100001', '01101110' ]
"""

import unittest

def word_to_bin(word):

    return []


class Test_word_to_bin(unittest.TestCase):
    def test_results(self):
        for word,exp in [ ('man', [ '01101101', '01100001', '01101110' ]),
            ('AB', ['01000001', '01000010']),
            ('wecking',[ '01110111', '01100101', '01100011', '01101011', '01101001', '01101110', '01100111' ] ),
            ('Ruby',[ '01010010', '01110101', '01100010', '01111001' ] ),
            ('Yosemite',[ '01011001', '01101111', '01110011', '01100101', '01101101', '01101001', '01110100', '01100101' ] ) ]:
            self.assertEqual(word_to_bin(word), exp)