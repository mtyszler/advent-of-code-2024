import pytest

from functions_day_03 import *


def test_read():
    s = parse_input('../input_files/input_day_03_example.txt')
    assert (s == 161)

def test_read2():
    s = parse_input_v2('../input_files/input_day_03_example_2.txt')
    assert (s == 48)