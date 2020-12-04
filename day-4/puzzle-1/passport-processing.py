import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
pattern = re.compile(r'([a-z]{3}):')
valid_count = 0

with open("input.txt") as file:
    found_fields = []
    for line in file:
        if line == '\n':
            val = [1 for field in found_fields if field in required_fields]
            if sum(val) == len(required_fields):
                valid_count += 1
            found_fields = []
        for match in re.findall(pattern, line):
            found_fields.append(match)

print(valid_count)
