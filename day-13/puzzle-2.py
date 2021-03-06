from functools import reduce

lines = open('input.txt').read().replace('\n\n', '\n').split('\n')[:-1]


# CRT directly stolen from Rosetta Code at:
# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

# end of the stolen part


buses = lines[1].split(',')
n = []
a = []
for i, bus in enumerate(buses):
    if bus.isnumeric():
        n.append(int(bus))
        if i == 0:
            a.append(0)
        else:
            a.append((i * -1) % int(bus))

print(chinese_remainder(n, a))
