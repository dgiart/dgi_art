import pytest
import sys

sys.path.insert(0, '..')
from task_08 import task8

def test_check_ip():
    # assert task8.check_ip('') == False
    assert task8.check_ip('12.3.4444') == False
    assert task8.check_ip('192.168.0.1') == True
    assert task8.check_ip('127.0.1.5') == True
