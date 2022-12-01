elf = 1
allcalself = []
calories = 0

with open("input.txt", "r") as inp:
    for line in inp:
        if line == "\n":
            allcalself.append({"elf": elf, "calories": calories})
            calories = 0
            elf += 1
        else:
            calories = calories + int(line)

top3 = []
for i in range(0, 3):
    best = 0
    index = 0
    for elfcals in allcalself:
        if elfcals["calories"] > allcalself[best]["calories"]:
            best = index
        index += 1
    best_index = allcalself.pop(best)
    top3.append(best_index)
total = 0
for a in top3:
    total += a["calories"]

print(f"part1 sol: {top3[0]['calories']}")
print(f"part2 sol: {total}")
