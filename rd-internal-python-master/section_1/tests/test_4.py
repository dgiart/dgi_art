import pytest
import sys

sys.path.insert(0, '..')
from task_04 import task4


def test_int_list():
    assert task4.max_value([-10, 0, 10, 999, 7]) == 999
    assert task4.min_value([-10, 0, 10, 999, 7]) == -10