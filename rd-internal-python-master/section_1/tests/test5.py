import pytest
import sys

sys.path.insert(0, '../..')
from task_05 import task5


def test_mults():
    assert task5.mults(3, 5, 10) == 23
    assert task5.mults(5, 3, 10) == 23
    assert task5.mults(3, 2, 10) == 32
    assert task5.mults(7, 8, 50) == 364

