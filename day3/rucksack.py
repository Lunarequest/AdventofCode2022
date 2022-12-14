from typing import Set
import string

priorities1 = 0
priorities2 = 0

weights = {}

#create dict with char to priority 
for x, y in zip(range(1, 53), string.ascii_lowercase+string.ascii_uppercase):
    weights[y] = x

group = []
with open("input.txt", "r") as inp:
    for line in inp:
        # part 1 each line is a compartment in a rucksack
        split = len(line) // 2
        compartment1 = set(line[0:split].strip())
        compartment2 = set(line[split:-1].strip())
        for common in compartment1.intersection(compartment2):
            priorities1 += weights[common]

        # part2 every 3 lines is a group of rucksacks
        group.append(line)
        if len(group) == 3:
            rucksack1:Set[str] = set(group[0].strip())
            rucksack2:Set[str] = set(group[1].strip())
            rucksack3:Set[str] = set(group[2].strip())
            for c in rucksack1.intersection(rucksack2).intersection(rucksack3):
                priorities2 += weights[c]
            group = []
print("part1: ", priorities1)
print("part2: ", priorities2)
