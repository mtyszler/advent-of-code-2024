import pytest

from functions_day_04 import *


def test_baby_example():
    m = parse_input('../input_files/input_day_04_example_1.txt')
    tot = find_word(m,'XMAS')
    assert (tot == 4)


def test_example():
    m = parse_input('../input_files/input_day_04_example_2.txt')
    tot = find_word(m,'XMAS')
    assert (tot == 18)


def test_baby_example_2():
    m = parse_input('../input_files/input_day_04_example_3.txt')
    tot = find_x_word(m,'MAS')
    assert (tot == 1)


def test_exampl_x():
    m = parse_input('../input_files/input_day_04_example_2.txt')
    tot = find_x_word(m, 'MAS')
    assert (tot == 9)