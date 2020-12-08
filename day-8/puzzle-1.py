import re

lines = open('input.txt').read().replace('\n\n', '\n').split('\n')

accumulator = 0
executed_lines = []

i = 0
while i < len(lines):
    if i in executed_lines:
        print(accumulator)
        break
    executed_lines.append(i)
    matches = re.match(r'(\S+) ([+-])(\d+)', lines[i])
    operation, argument_plus_minus, argument_num = matches.group(1, 2, 3)
    argument_num = int(argument_num)
    if operation == 'acc':
        if argument_plus_minus == '+':
            accumulator += argument_num
        else:
            accumulator -= argument_num
        i += 1
    if operation == 'jmp':
        if argument_plus_minus == '+':
            i += argument_num
        else:
            i -= argument_num
    if operation == 'nop':
        i += 1
