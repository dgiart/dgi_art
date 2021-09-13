import pytest
import sys

sys.path.insert(0, '..')
from task_02 import task2

list_to_test = [1, 2., 'a', {1:'one'}, (1,2), 3]
result = [1, 3]

def test_filter_list1():
    assert task2.filter_list1(list_to_test) == result


def test_filter_list2():
    assert task2.filter_list2(list_to_test) == result


def test_filter_list3():
    assert task2.filter_list3(list_to_test) == result