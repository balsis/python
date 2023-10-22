import pytest

def sum_it(x, y):
    return x + y

def test_1():
    assert sum_it(4, 8) == 12, 'Wrong'

def test_2():
    assert sum_it(5, 12) == 15, 'Wrong'