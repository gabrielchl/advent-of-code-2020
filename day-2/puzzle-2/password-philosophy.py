import re

valid_count = 0

with open("input.txt") as file:
    for line in file:
        matches = re.match(r"(\d+)-(\d+) ([a-zA-Z]): (.+)", line)
        first, second, char, pw = matches.group(1, 2, 3, 4)
        first = int(first) - 1
        second = int(second) - 1
        if (pw[first] == char and pw[second] != char or pw[first] != char and pw[second] == char):
            valid_count += 1

print(valid_count)
