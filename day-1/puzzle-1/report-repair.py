import sys

entries = []

with open("input.txt") as file:
    for line in file:
        entries.append(int(line))

    for entry1 in entries:
        for entry2 in entries:
            if entry1 + entry2 == 2020:
                print(entry1 * entry2)
                sys.exit()
