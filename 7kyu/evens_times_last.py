"""
Given a sequence of integers, return the sum of all the integers that have an even index,
multiplied by the integer at the last index.

Indexes in sequence start from 0.

If the sequence is empty, you should return 0.
"""


def even_last(numbers):
    """
    My solution
    """
    return sum(numbers[i] for i in range(len(numbers)) if i % 2 == 0) * numbers[-1] if len(numbers) != 0 else 0

def even_last(numbers):
    """
    Best solution / Clever solution
    """
    return sum(numbers[::2]) * numbers[-1] if numbers else 0

print(even_last([2, 3, 4, 5])) #, 30
print(even_last([])) #0