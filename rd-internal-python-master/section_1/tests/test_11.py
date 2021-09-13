import pytest
import sys

sys.path.insert(0, '..')
from task_11.task11 import Sum_of_elements

summa = 0
l1 = [1, 2, 3]
l2 = [1, [5, 6, [13, 5]], 2, 3, [2, [-5, 6, [-7, [], 8]]], -50]
l3 = [1, [5, 6, [13, 5]], 2, 3, [2, [-5, 6, [-7, [], 8]]], -50]
l4 = [1, [5, 6, [13, 5]], 2, 3, [2, [-5, 6, [-7, [], 8]]], -50]
l4 = [[3, 4]]

def test_sum_of_elements1():
    s = s = Sum_of_elements()
    assert s.sum_of_elements(l1) == 6


def test_sum_of_elements2():
    s = Sum_of_elements()
    res = s.sum_of_elements(l2)
    assert res == -11


def test_sum_of_elements3():
    s = Sum_of_elements()
    res = s.sum_of_elements(l3)
    assert res == -11
