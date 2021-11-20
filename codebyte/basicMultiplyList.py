#[1,2,3,4]
## [1,4,9,16]
import pytest

ndouble = []
def double(n):
    return [i*i for i in n]


def test_double():
    assert(double([1,2,3,4]) == [1,4,9,16])
    assert(double([]) == [])
    assert(double([0]) == [0])
    assert(double([0]) == [0])
    assert(double([-1, 2]) == [1, 4])
