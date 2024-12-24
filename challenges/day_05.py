from functions_day_05 import *

# challenge 1
ord, instr = parse_input('../input_files/input_day_05.txt')

corr, incorr = assess_instructions(instr, ord)

tot = 0
for x in corr:
    i = int((len(x)-1)/2)
    tot += x[i]

print(tot)

# challenge 2:
correct_incorrect = []
for x in incorr:
    correct_incorrect.append(fix_instruction(x, ord))

tot = 0
for x in correct_incorrect:
    i = int((len(x)-1)/2)
    tot += x[i]

print(tot)

# challenge 2






