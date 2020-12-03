pt_x = 0
tree_counter = 0

with open("input.txt") as file:
    for line in file:
        if line[pt_x] == '#':
            tree_counter += 1
        pt_x += 3
        if pt_x >= len(line) - 1:
            pt_x -= len(line) - 1

print(tree_counter)
