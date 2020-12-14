import re

lines = open('input.txt').read().replace('\n\n', '\n').split('\n')[:-1]

current_mask = ''
memory = {}

for line in lines:
    if line[0:4] == 'mask':
        current_masks = []
        current_mask = line[7:]
    else:
        matches = re.match(r'mem\[(\d+)\] = (\d+)', line)
        memory_addr, value = matches.group(1, 2)
        memory_addr = str('{0:036b}'.format(int(memory_addr)))
        new_mask = ''
        for i, digit_mask in enumerate(current_mask):
            if digit_mask == '0':
                new_mask += memory_addr[i]
            elif digit_mask == '1':
                new_mask += '1'
            elif digit_mask == 'X':
                new_mask += 'X'

        xes = current_mask.count('X')
        for i in range(2 ** xes):
            format_str = '{0:0' + str(xes) + 'b}'
            xes_value = str(format_str.format(i))
            new_memory_addr = new_mask
            for j in xes_value:
                new_memory_addr = new_memory_addr.replace('X', j, 1)
            memory[int(new_memory_addr, 2)] = int(value)

count = 0
for value in memory:
    count += memory[value]
print(count)
