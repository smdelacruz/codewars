# unittest sample
# import unittest

# def basic_multiply(a,b):
#     return a * b

# class TestFunction(unittest.TestCase):
#     def test_func(self):
#         self.assertEqual(basic_multiply(6,3), 18)
#         self.assertEqual(basic_multiply(0,3), 0)




# pytest sample
def basic_multiply(a,b):
    return a * b

def test_func():
    assert basic_multiply(6,3) == 18
    assert basic_multiply(0,3) == 0