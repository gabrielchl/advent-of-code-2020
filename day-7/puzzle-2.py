import re

bags = []


def count_child_with_parent(parent):
    childs = []  # count, child, sub-count
    for bag in bags:
        if bag[0] == parent:
            result = [bag[1], bag[2], count_child_with_parent(bag[2]) + 1]
            childs.append(result)
    counter = 0
    for child in childs:
        if not child[2]:
            child[2] = 1
        counter += int(child[0]) * child[2]
    return counter


lines = open('input.txt').read().replace('\n\n', '\n').split('\n')

counter = 0
final_mul = 1

for line in lines:
    if not line:
        continue
    matches = re.match(r'(.+) bags contain (.+)', line)
    parent, raw_childs = matches.group(1, 2)
    childs = re.findall(r'(\d+) (.+?) bag', raw_childs)
    for child in childs:
        bags.append([parent, child[0], child[1]])

print(count_child_with_parent('shiny gold'))
