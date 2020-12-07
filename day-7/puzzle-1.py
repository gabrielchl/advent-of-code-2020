import re

bags = []


def count_parent_with_child(child):
    parents = []
    for bag in bags:
        if bag[1] == child:
            parents.append(bag[0])
            parents.extend(count_parent_with_child(bag[0]))
    return list(set(parents))


lines = open('input.txt').read().replace('\n\n', '\n').split('\n')

for line in lines:
    if not line:
        continue
    matches = re.match(r'(.+) bags contain (.+)', line)
    parent, raw_childs = matches.group(1, 2)
    childs = re.findall(r'\d+ (.+?) bag', raw_childs)
    for child in childs:
        bags.append([parent, child])

print(len(count_parent_with_child('shiny gold')))
