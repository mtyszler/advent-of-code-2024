def parse_input(filename: str) -> [dict, list[list]]:
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    ordering = {}
    instructions = []

    ordering_block = True
    for this_line in lines:
        if this_line == "\n":
            ordering_block = False
            continue

        if ordering_block:
            before, after = this_line.strip().split("|")
            before = int(before)
            after = int(after)
            if before not in ordering.keys():
                ordering[before] = {'before': list(), 'after': list()}
            if after not in ordering.keys():
                ordering[after] = {'before': list(), 'after': list()}
            ordering[before]['after'].append(after)
            ordering[after]['before'].append(before)
        else:
            instructions.append([int(x) for x in this_line.strip().split(',')])

    return ordering, instructions


def assess_instructions(instructions: list[list], ordering: dict) -> [list, list]:
    corr = []
    incorr = []
    for instruction in instructions:
        correct_order = True
        for i in range(len(instruction)):
            cur = instruction[i]
            before = instruction[0:i]
            after = instruction[i + 1:]

            if any([b not in ordering[cur]['before'] for b in before]):
                correct_order = False
                break
            if any([a not in ordering[cur]['after'] for a in after]):
                correct_order = False
                break

        if correct_order:
            corr.append(instruction)
        else:
            incorr.append(instruction)

    return corr, incorr


def fix_instruction(instruction: list, ordering: dict) -> list:
    correct_order = True
    temp_instruction = instruction.copy()
    to_fix = []
    for i in range(len(instruction)):
        cur = instruction[i]
        before = instruction[0:i]
        after = instruction[i + 1:]

        if any([b not in ordering[cur]['before'] for b in before]):
            correct_order = False
            if cur not in to_fix:
                to_fix.append(cur)
            if cur in temp_instruction:
                temp_instruction.remove(cur)

        if any([a not in ordering[cur]['after'] for a in after]):
            correct_order = False
            if cur not in to_fix:
                to_fix.append(cur)
            if cur in temp_instruction:
                temp_instruction.remove(cur)

    if correct_order:
        return instruction
    else:
        for x in to_fix:
            temp_instruction = add_to_list(x, temp_instruction, ordering)

        return temp_instruction


def add_to_list(item: int, original_instruction:list, ordering: dict)->list:
    if not original_instruction:
        return [item]
    for i in range(len(original_instruction)):
        cur = original_instruction[i]
        before = original_instruction[0:i]
        after = original_instruction[i + 1:]

        new_tentative_instruction = before + [item] + [cur] + after
        cor , _ = assess_instructions([new_tentative_instruction], ordering)
        if cor == [new_tentative_instruction]:
            return cor[0]
        else:
            new_tentative_instruction = before + [cur] + [item] + after
            cor, _ = assess_instructions([new_tentative_instruction], ordering)
            if cor == [new_tentative_instruction]:
                return cor[0]

