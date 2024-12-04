import pytest

from functions_day_02 import *


def test_safe():
    s = parse_input('../input_files/input_day_02_example.txt')
    assert (s == 2)

def test_safe_dampener():
    s = parse_input('../input_files/input_day_02_example.txt', dampener=True)
    assert (s == 4)