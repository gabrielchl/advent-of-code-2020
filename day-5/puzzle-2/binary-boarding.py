import math

seat_ids = []


def binary_space_partitioning(str, min, max, lower, upper):
    for char in str:
        if char == lower:
            max = math.floor((min + max) / 2)
        if char == upper:
            min = math.ceil((min + max) / 2)
    return min


with open("input.txt") as file:
    for line in file:
        row = binary_space_partitioning(line[0:7], 0, 127, 'F', 'B')
        col = binary_space_partitioning(line[7:10], 0, 7, 'L', 'R')
        seat_ids.append(row * 8 + col)

min = min(seat_ids)
max = max(seat_ids)
for seat_id in range(min, max):
    if seat_id not in seat_ids:
        print(seat_id)
