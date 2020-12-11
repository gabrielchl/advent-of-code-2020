lines = open('input.txt').read().replace('\n\n', '\n').split('\n')[:-1]

for i in range(0, len(lines)):
    lines[i] = int(lines[i])

lines.append(0)
lines.append(max(lines) + 3)
lines.sort()

sections = []

for i, line in enumerate(lines):
    if i == 0:
        continue
    if lines[i] == lines[i - 1] + 3:
        sections.append(lines[i - 1])

paths = 1
last_end = 0
for section in sections:
    solutions = [[last_end]]
    new_solutions = []
    for i in range(0, section - last_end):
        for solution in solutions:
            if solution[-1] >= section:
                continue
            for j in range(1, 4):
                if solution[-1] + j in lines and solution + [solution[-1] + j] not in new_solutions:
                    new_solutions.append(solution + [solution[-1] + j])
            last_end = section
        solutions = new_solutions

    count = 0
    for solution in new_solutions:
        if solution[-1] == section:
            count += 1
    paths *= count
    print(count)
    print(solutions)
print(paths)
print(lines)
print(sections)
