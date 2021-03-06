# yes, i no longer care about efficiency at this point lol

import numpy as np

input = open('input.txt').read().replace('\n\n', '\n').split('\n')[:-1]


def get_neighbours(matrix, w, z, y, x):
    active_count = 0
    inactive_count = 0
    for dw in range(-1, 2):
        if w + dw < 0 or w + dw >= len(matrix):
            continue
        for dz in range(-1, 2):
            if z + dz < 0 or z + dz >= len(matrix):
                continue
            for dy in range(-1, 2):
                if y + dy < 0 or y + dy >= len(matrix):
                    continue
                for dx in range(-1, 2):
                    if x + dx < 0 or x + dx >= len(matrix):
                        continue
                    if dw == 0 and dz == 0 and dy == 0 and dx == 0:
                        continue
                    neighbour = matrix[w + dw][z + dz][y + dy][x + dx]
                    if neighbour == b'#':
                        active_count += 1
                    elif neighbour == b'.':
                        inactive_count += 1
    return (active_count, inactive_count)


cycles = 6
size = len(input)
final_size = len(input) + cycles * 2
if final_size % 2 == 0:
    final_size += 1
matrix = np.chararray((final_size, final_size, final_size, final_size))
matrix[:] = '.'

mid_index = int((final_size - 1) / 2)
start_index = int(mid_index - size / 2)

for y, row in enumerate(input):
    matrix[mid_index][mid_index][start_index + y][start_index:start_index + len(row)] = list(row)

for _ in range(6):
    new_matrix = np.chararray((final_size, final_size, final_size, final_size))
    new_matrix[:] = '.'
    for w, block in enumerate(matrix):
        for z, slice in enumerate(block):
            for y, row in enumerate(slice):
                for x, cube in enumerate(row):
                    (active_count, inactive_count) = get_neighbours(matrix, w, z, y, x)
                    if cube == b'#':
                        if active_count == 2 or active_count == 3:
                            new_matrix[w][z][y][x] = '#'
                        else:
                            new_matrix[w][z][y][x] = '.'
                    elif cube == b'.':
                        if active_count == 3:
                            new_matrix[w][z][y][x] = '#'
                        else:
                            new_matrix[w][z][y][x] = '.'
    matrix = new_matrix

counter = 0
for block in matrix:
    for slice in block:
        for row in slice:
            for cube in row:
                if cube == b'#':
                    counter += 1
print(counter)
