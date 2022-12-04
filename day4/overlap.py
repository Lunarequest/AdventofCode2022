overlaps_complete = 0
overlaps_at_all = 0

with open("input.txt", "r") as file:
    for line in file:
        pairs = line.strip().split(",")
        elf1 = []
        elf2 = []
        # elf1
        start = int(pairs[0].split("-")[0])
        end = int(pairs[0].split("-")[1])
        for i in range(start, end + 1):
            elf1.append(i)
        # elf2
        start = int(pairs[1].split("-")[0])
        end = int(pairs[1].split("-")[1])
        for i in range(start, end + 1):
            elf2.append(i)
        merged = set(elf1).union(set(elf2))
        if len(merged) == len(elf1) or len(merged) == len(elf2):
            overlaps_complete += 1
        if len(merged) != len(elf1) + len(elf2):
            overlaps_at_all += 1

print(f"part1: {overlaps_complete}")
print(f"part2: {overlaps_at_all}")
