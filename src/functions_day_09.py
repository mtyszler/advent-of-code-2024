def parse_input(filename: str) -> list:
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    disk = []

    free = False
    id_ = 0
    for this_line in lines:
        for p in this_line.strip():
            if not free:
                disk.extend([str(id_)] * int(p))
                free = True
            else:
                disk.extend(['.'] * int(p))
                id_ += 1
                free = False

    return disk


def rearrange_disk(disk: list) -> list:
    print(len(disk))
    disk_as_str = ''.join(disk)
    left, right = disk_as_str.split('.', maxsplit=1)
    pos = -1
    while set(right) != {'.'}:
        max_right = disk[pos]
        while max_right == '.':
            pos -= 1
            print(pos)
            max_right = disk[pos]
        blank = disk.index('.')
        disk[blank] = max_right
        disk[pos] = '.'
        disk_as_str = ''.join(disk)
        left, right = disk_as_str.split('.', maxsplit=1)

    return disk


def rearrange_disk_2(disk: list) -> list:
    cur_id = disk[-1]
    empty_spaces = []
    pos_start = -999
    for pos, x in enumerate(disk):
        this_x = 0
        if x == '.':
            if pos_start == -999:
                pos_start = pos
            this_x +=1
        else:
            empty_spaces.append(pos_start, this_x)
            pos_start=-99
            this_x=0

    while True:
        indices = [i for i, x in enumerate(disk) if x == str(cur_id)]
        n_space = len(indices)
            pos -= 1
            print(pos)
            max_right = disk[pos]
        blank = disk.index('.')
        disk[blank] = max_right
        disk[pos] = '.'
        disk_as_str = ''.join(disk)
        left, right = disk_as_str.split('.', maxsplit=1)

    return disk


def check_sum(disk: list) -> float:
    total = 0
    for pos, id_ in enumerate(disk):
        if id_ == '.':
            break
        total += pos * int(id_)

    return total
