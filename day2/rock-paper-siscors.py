scorep1 = 0
scorep2 = 0

points = {"x": 1, "y": 2, "z": 3}
maps = {"a": "x", "b": "y", "c": "z"}
weak = {"a": "z", "b": "x", "c": "y"}
wins = {"a": "y", "b": "z", "c": "x"}


def getscore1(opp: str, us: str) -> int:
    opp = opp.replace("a", "x").replace("b", "y").replace("c", "z")
    if opp == us:
        return 3 + points[us]
    else:
        if (
            (opp == "x" and us == "z")  # rock beats sicssors
            or (opp == "y" and us == "x")  # papaer beats rock
            or (opp == "z" and us == "y")  # sciscors beats paper
        ):
            return 0 + points[us]
        else:
            return 6 + points[us]


def getscore2(opp: str, win: str) -> int:
    if win == "x":
        return points[weak[opp]]
    elif win == "y":
        return 3 + points[maps[opp]]
    else:
        return 6 + points[wins[opp]]


with open("input.txt", "r") as input:
    for line in input:
        x = line.lower().strip().split(" ")
        scorep1 += getscore1(x[0], x[1])
        scorep2 += getscore2(x[0], x[1])

print(f"part1: {scorep1}\npart2: {scorep2}")
