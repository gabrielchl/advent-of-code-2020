import math

max_seat_id = 0


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
        seat_id = row * 8 + col
        if seat_id > max_seat_id:
            max_seat_id = seat_id

print(max_seat_id)
