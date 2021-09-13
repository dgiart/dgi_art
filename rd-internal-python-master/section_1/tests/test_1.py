import pytest
import sys

sys.path.insert(0, '..')
for el in sys.path:
    print(el)

from task_01 import task1

check_password = task1.check_password


def test_short_password():
    assert check_password('aaa') == False

def test_lower_password():
    assert check_password('aaaaaaaaaaaaaaaaaa') == False

def test_upper_password():
    assert check_password('AGKGFEGCJOPIRFSFJ') == False

def test_correct_password():
    assert check_password('1PaaLGHkgbcgly') == True
