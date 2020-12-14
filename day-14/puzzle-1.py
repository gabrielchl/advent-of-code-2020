import re

lines = open('input.txt').read().replace('\n\n', '\n').split('\n')[:-1]

current_mask = 0
memory = [0] * 70000

for line in lines:
    if line[0:4] == 'mask':
        current_mask = line[7:]
    else:
        matches = re.match(r'mem\[(\d+)\] = (\d+)', line)
        memory_addr, value = matches.group(1, 2)
        value = str('{0:036b}'.format(int(value)))
        masked_value = ''
        for i, digit_mask in enumerate(current_mask):
            if digit_mask != 'X':
                masked_value += digit_mask
            else:
                masked_value += value[i]
        memory[int(memory_addr)] = int(masked_value, 2)

print(sum(memory))
