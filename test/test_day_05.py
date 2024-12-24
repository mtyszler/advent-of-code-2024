import pytest

from functions_day_05 import *


def test_example():
    ord, instr = parse_input('../input_files/input_day_05_example.txt')

    corr, incorr = assess_instructions(instr, ord)

    tot = 0
    for x in corr:
        i = int((len(x)-1)/2)
        tot += x[i]
    assert (tot == 143)

def test_example_fixing():
    ord, instr = parse_input('../input_files/input_day_05_example.txt')

    corr, incorr = assess_instructions(instr, ord)

    correct_incorrect = []
    for x in incorr:
        correct_incorrect.append(fix_instruction(x, ord))

    tot = 0
    for x in correct_incorrect:
        i = int((len(x)-1)/2)
        tot += x[i]
    assert (tot == 123)

