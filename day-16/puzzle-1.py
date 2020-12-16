import re

[rules, _, tickets] = open('input.txt').read().split('\n\n')

ranges = []

rules = rules.split('\n')
for rule in rules:
    matches = re.match(r'\D+(\d+)-(\d+) or (\d+)-(\d+)', rule)
    min_1, max_1, min_2, max_2 = matches.group(1, 2, 3, 4)
    ranges.append([int(min_1), int(max_1)])
    ranges.append([int(min_2), int(max_2)])

error_rate = 0
tickets = tickets.split('\n')[1:-1]
for ticket in tickets:
    values = [int(el) for el in ticket.split(',')]
    for value in values:
        in_range = False
        for range in ranges:
            if range[0] <= value <= range[1]:
                in_range = True
                break
        if not in_range:
            error_rate += value

print(error_rate)
