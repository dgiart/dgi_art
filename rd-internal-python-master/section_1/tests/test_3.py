import pytest
import sys

sys.path.insert(0, '..')
from task_03 import task3

text_to_test = '''
a bcb ccc Cc findme Findme _FindMe    Findme_a,
findMe, findme. c
'''


def test_letter_counter1():
    assert task3.letter_counter1(text_to_test) == (7, 'c')

def test_python_counter():
    assert task3.python_counter(text_to_test, 'findme') == 4
