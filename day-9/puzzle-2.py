import sys

lines = open('input.txt').read().replace('\n\n', '\n').split('\n')

for i, line in enumerate(lines):
    lines[i] = int(lines[i])
    if i < 25:
        continue
    found_pair = False
    for j in range(i - 25, i):
        if lines[i] - lines[j] in lines[i - 25: i]:
            found_pair = True
    if not found_pair:
        for j in range(i):
            for k in range(i):
                if sum(lines[j: k]) == lines[i]:
                    print(min(lines[j: k]) + max(lines[j: k]))
                    sys.exit()
