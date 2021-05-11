"""
Examples
[2, 3, 4, 1]  =>  [4, 1, 2, 3]
[1, 3, 2]     =>  [1, 3, 2]
[1, 2]        =>  [1, 2]
First example step-by-step explanation (note: the explanation uses 1-based indexing to make the correspondence with friend-numbering clearer):

The friend 1 gave gift to the friend 2 (a[1] == 2) - this means that in the output array number 1 is at position 2 : [_, 1, _, _].
The friend 2 gave gift to the friend 3 (a[2] == 3) - this means that in the output array number 2 is at position 3 : [_, 1, 2, _].
The friend 3 gave gift to the friend 4 (a[3] == 4) - this means that in the output array number 3 is at position 4 : [_, 1, 2, 3].
The friend 4 gave gift to the friend 1 (a[4] == 1) - this means that in the output array number 4 is at position 1 : [4, 1, 2, 3].
"""
import unittest

def presents(lst):
    """
    My solution
    """
    p = []
    for i, v in enumerate(lst, start=1):
        print("index[{}] = value [{}]".format(i, v))
        p[v] = v
    print(p)
print(presents([2, 3, 4, 1]))
# class TestMygcd(unittest.TestCase):
#     def test_results(self):
#         self.assertEqual(presents([2, 3, 4, 1]), [4, 1, 2, 3])
#         self.assertEqual(presents([1, 3, 2]), [1,3,2])
#         self.assertEqual(presents([1,2]), [1,2])
