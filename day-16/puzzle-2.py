import re

[rules, my_ticket, tickets] = open('input.txt').read().split('\n\n')

ranges = []

rules = rules.split('\n')
for rule in rules:
    matches = re.match(r'\D+(\d+)-(\d+) or (\d+)-(\d+)', rule)
    min_1, max_1, min_2, max_2 = matches.group(1, 2, 3, 4)
    ranges.append([int(min_1), int(max_1)])
    ranges.append([int(min_2), int(max_2)])

tickets = tickets.split('\n')[1:-1]
valid_tickets = []
for ticket in tickets:
    values = [int(el) for el in ticket.split(',')]
    valid = True
    for value in values:
        in_range = False
        for range_val in ranges:
            if range_val[0] <= value <= range_val[1]:
                in_range = True
                break
        if not in_range:
            valid = False
            break
    if valid:
        valid_tickets.append(ticket)

ranges = ranges[:20 * 2]
ranges = [list(el) for el in zip(ranges[0::2], ranges[1::2])]
fields = {}
for field in range(20):
    fields[field] = list(range(20))

for ticket in valid_tickets:
    values = [int(el) for el in ticket.split(',')]
    for i, value in enumerate(values):
        for j, range_val in enumerate(ranges):
            remove = True
            for range_val_val in range_val:
                if range_val_val[0] <= value <= range_val_val[1]:
                    remove = False
                    break
            if remove and i in fields[j]:
                fields[j].remove(i)

for i in range(20):
    for field in fields:
        if len(fields[field]) == 1:
            for field_1 in fields:
                if fields[field][0] in fields[field_1] and field != field_1:
                    fields[field_1].remove(fields[field][0])

my_ticket = my_ticket.split('\n')[1]
my_ticket = [int(el) for el in my_ticket.split(',')]
counter = 1
for i, field in enumerate(fields):
    if i == 6:
        break
    counter *= my_ticket[fields[field][0]]

print(counter)
