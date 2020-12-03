slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]
tree_mul = 1

for slope in slopes:
    pt_x = 0
    tree_counter = 0
    with open("input.txt") as file:
        line_counter = slope[1] - 1
        for line in file:
            line_counter += 1
            if line_counter % slope[1]:
                continue
            if line[pt_x] == '#':
                tree_counter += 1
            pt_x += slope[0]
            if pt_x >= len(line) - 1:
                pt_x -= len(line) - 1

    tree_mul *= tree_counter

print(tree_mul)
