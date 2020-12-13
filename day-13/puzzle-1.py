import math

lines = open('input.txt').read().replace('\n\n', '\n').split('\n')[:-1]

depart_time = int(lines[0])
buses = [int(el) for el in lines[1].split(',') if el != 'x']
times = []

for bus in buses:
    new_time = math.ceil(depart_time / bus)
    times.append(new_time * bus)

print((min(times) - depart_time) * buses[times.index(min(times))])
