def distance(list_1: list, list_2: list) -> float:

    list_1_s = sorted(list_1)
    list_2_s = sorted(list_2)

    d = 0
    for x, y in zip(list_1_s, list_2_s):
        d += abs(x-y)

    return d


def parse_input(filename: str) -> [list, list]:
    input_file = open(filename, 'r')
    lines = input_file.readlines()

    list_1 = []
    list_2 = []

    for this_line in lines:
        item_1, item_2 = this_line.strip().split()

        list_1.append(int(item_1))
        list_2.append(int(item_2))

    return list_1, list_2


def similarity(list_1: list, list_2: list) -> float:

    s = 0
    for x in list_1:
        n = list_2.count(x)
        s += x*n

    return s
