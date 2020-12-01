import sys

entries = []

with open("input.txt") as file:
    for line in file:
        entries.append(int(line))

    for entry1 in entries:
        for entry2 in entries:
            for entry3 in entries:
                if entry1 + entry2 + entry3 == 2020:
                    print(entry1 * entry2 * entry3)
                    sys.exit()
