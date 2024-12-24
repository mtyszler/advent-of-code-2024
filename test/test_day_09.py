import pytest

from functions_day_09 import *


def test_baby_example():
    disk = parse_input('../input_files/input_day_09_baby_example.txt')

    arranged_disk = rearrange_disk(disk)

    assert (''.join(arranged_disk) == '022111222......')

def test_example():
    disk = parse_input('../input_files/input_day_09_example.txt')

    arranged_disk = rearrange_disk(disk)

    tot = check_sum(arranged_disk)

    assert (tot == 1928)
