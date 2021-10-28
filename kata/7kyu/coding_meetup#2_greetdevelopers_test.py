"""
You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising.

Your task is to return an object (associative array in PHP) which includes the count of each coding language represented at the meetup.

For example, given the following input array:

list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
    { 'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
    ]
your function should return the following object (associative array in PHP):

{ 'C': 2, 'JavaScript': 1, 'Ruby': 1 }
Notes:

The order of the languages in the object does not matter.
The count value should be a valid number.
The input array will always be valid and formatted as in the example above.
"""
import unittest

def greet_developers(lst):
    """
    My solution
    """
    for i in lst:
        i['greeting'] = "Hi {name}, what do you like the most about {language}?".format(name=i['firstName'], language=i['language'])
    return lst


class TestMygcd(unittest.TestCase):
    def test_results(self):
        list1 = [
            {'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35,
             'language': 'Java'},
            {'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35,
             'language': 'Python'},
            {'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32,
             'language': 'Ruby'}
        ]
        answer = [
            {'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35,
             'language': 'Java',
             'greeting': 'Hi Sofia, what do you like the most about Java?'
             },
            {'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35,
             'language': 'Python',
             'greeting': 'Hi Lukas, what do you like the most about Python?'
             },
            {'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32,
             'language': 'Ruby',
             'greeting': 'Hi Madison, what do you like the most about Ruby?'
             }
        ]
        self.assertEqual(greet_developers(list1), answer)
