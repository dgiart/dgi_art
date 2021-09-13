import pytest
import sys

sys.path.insert(0, '..')
from task_07 import task7

def test_file_size():
    assert task7.file_size(19) == '19.0B'
    assert task7.file_size(12345) == '12.1Kb'
    assert task7.file_size(1101947) == '1.1Mb'
    assert task7.file_size(999999999999) == '931.3Gb'
    assert task7.file_size(12389485008592) == '11.3Tb'
    assert task7.file_size(1238948500859265434) == 'File Size is out of range'
