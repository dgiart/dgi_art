import pytest
from ..task_01 import task1

def test_password():
    assert task1.check_password('aaa') == True