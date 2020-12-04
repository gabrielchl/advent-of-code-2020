import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
pattern = re.compile(r'([a-z]{3}):(\S+)')
valid_count = 0

with open("input.txt") as file:
    found_fields = []
    all_valid = True
    for line in file:
        if line == '\n':
            val = [1 for field in found_fields if field in required_fields]
            if all_valid and sum(val) == len(required_fields):
                valid_count += 1
            found_fields = []
            all_valid = True
        if not all_valid:
            continue
        for (field, value) in re.findall(pattern, line):
            found_fields.append(field)
            if field == 'byr':
                if len(value) != 4 or int(value) < 1920 or int(value) > 2002:
                    all_valid = False
                    break
            if field == 'iyr':
                if len(value) != 4 or int(value) < 2010 or int(value) > 2020:
                    all_valid = False
                    break
            if field == 'eyr':
                if len(value) != 4 or int(value) < 2020 or int(value) > 2030:
                    all_valid = False
                    break
            if field == 'hgt':
                if value[-2:] == 'cm':
                    if int(value[:-2]) < 150 or int(value[:-2]) > 193:
                        all_valid = False
                        break
                elif value[-2:] == 'in':
                    if int(value[:-2]) < 59 or int(value[:-2]) > 76:
                        all_valid = False
                        break
                else:
                    all_valid = False
                    break
            if field == 'hcl':
                local_valid = [char for char in value[1:] if char not in ['a', 'b', 'c', 'd', 'e', 'f'] and not char.isnumeric()]
                if local_valid or len(value) != 7 or value[0] != '#':
                    all_valid = False
                    break
            if field == 'ecl':
                if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    all_valid = False
                    break
            if field == 'pid':
                if len(value) != 9 or not value.isnumeric():
                    all_valid = False
                    break

print(valid_count)
