"""
In this kata, you will do addition and subtraction on a given string. The return value must be also a string.

Note: the input will not be empty.

Examples

"1plus2plus3plus4"  --> "10"
"1plus2plus3minus4" -->  "2"
"""
import unittest
def calculate(s):
    new_s = ""
    new_s = s.replace("plus", "+").replace("minus", "-")
    holder = 0
    for i in new_s:
        i = int(i)
        if i == "+":
            holder =+i
        elif i == "-":
            holder =-i
        else: holder = i
    return holder

print(calculate('1plus2plus3plus4'))
print(calculate('1plus2plus3minus4'))
class Test_calculate(unittest.TestCase):
    def test_results(self):
        self.assertEqual(calculate('1plus2plus3plus4'),'10')
        self.assertEqual(calculate('1minus2minus3minus4'),'-8')
        self.assertEqual(calculate('1plus2plus3minus4'),'2')