import re

valid_count = 0

with open("input.txt") as file:
    for line in file:
        matches = re.match(r"(\d+)-(\d+) ([a-zA-Z]): (.+)", line)
        min, max, char, pw = matches.group(1, 2, 3, 4)
        pw = [pwchar for pwchar in pw if pwchar == char]
        if len(pw) >= int(min) and len(pw) <= int(max):
            valid_count += 1

print(valid_count)
