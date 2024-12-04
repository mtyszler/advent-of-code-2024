import re


def mul(x,y):
    return  x * y


def parse_input(filename: str) -> int:
    input_file = open(filename, 'r')
    lines = input_file.readlines()

    total = 0

    # Regex pattern to match only `mul(x,y)`
    pattern = r"mul\(\d+,\d+\)"
    for this_line in lines:

        # Find all matches
        matches = re.findall(pattern, this_line)
        total += sum([eval(x) for x in matches])

    return total

def parse_input_v2(filename: str) -> int:
    input_file = open(filename, 'r')
    lines = input_file.readlines()

    total = 0

    # Regex pattern to match only `mul(x,y)`
    pattern = r"mul\(\d+,\d+\)"
    for this_line in lines:

        all_chunks = this_line.split("do()")

        for chunk in all_chunks:
            dos = chunk.split("don't()")[0]

            # Find all matches

            matches = re.findall(pattern, dos)
            total += sum([eval(x) for x in matches])

    return total