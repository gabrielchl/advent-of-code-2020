import sys

lines = open('input.txt').read().replace('\n\n', '\n').split('\n')

for i, line in enumerate(lines):
    if i < 25:
        continue
    found_pair = False
    for j in range(i - 25, i):
        if str(int(lines[i]) - int(lines[j])) in lines[i - 25: i]:
            found_pair = True
    if not found_pair:
        print(lines[i])
        sys.exit()
