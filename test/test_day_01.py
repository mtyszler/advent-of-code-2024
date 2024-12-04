import pytest

from functions_day_01 import *


def test_distance():
    list_1, list_2 = parse_input('../input_files/input_day_01_example.txt')
    d = distance(list_1, list_2)
    assert (d == 11)


def test_similarity():
    list_1, list_2 = parse_input('../input_files/input_day_01_example.txt')
    s = similarity(list_1, list_2)
    assert (s == 31)
