instructions = open('input.txt').read().replace('\n\n', '\n').split('\n')[:-1]

x = y = 0
dir = 0

for instruction in instructions:
    action = instruction[0]
    value = int(instruction[1:])

    if action == 'N':
        y += value
    elif action == 'S':
        y -= value
    elif action == 'E':
        x += value
    elif action == 'W':
        x -= value
    elif action == 'L':
        dir -= value / 90
        dir = dir % 4
    elif action == 'R':
        dir += value / 90
        dir = dir % 4
    elif action == 'F':
        if dir == 0:  # east
            x += value
        elif dir == 2:  # west
            x -= value
        elif dir == 1:  # south
            y -= value
        elif dir == 3:  # north
            y += value

print(abs(x) + abs(y))
