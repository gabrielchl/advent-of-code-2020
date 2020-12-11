lines = open('input.txt').read().replace('\n\n', '\n').split('\n')[:-1]

for i in range(0, len(lines)):
    lines[i] = int(lines[i])

i = 0
jump_counts = [0, 0, 0]
jolt = 0
while i < len(lines):
    for j in range(1, 4):
        if jolt + j in lines:
            jump_counts[j - 1] += 1
            jolt = jolt + j
            break
    i += 1

jump_counts[2] += 1
print(jump_counts[0] * jump_counts[2])
