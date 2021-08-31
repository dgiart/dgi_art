import pytest
import sys

sys.path.insert(0, '../..')
from task_11 import task11

summa = 0
l1 = [1, 2, 3]
l2 = [1, [5, 6, [13, 5]], 2, 3, [2, [-5, 6, [-7, [], 8]]], -50]
l3 = [1, [], 2, [-19, 700, 0, [90, 33, [18, 77, [0, ], -2], 11, 16], -100]]
l4 = [[3, 4]]


def test_sum_of_elements1():
    assert task11.sum_of_elements(l1) == 6


def test_sum_of_elements2():
    assert task11.sum_of_elements(l2) == -11


def test_sum_of_elements3():
    assert task11.sum_of_elements(l3) == 827
