from typing import Dict, Set


#################### Template ####################
with open("puzzle.txt") as f:
    lines = f.readlines()
#################### Template ####################


pages: Dict[int, Set[int]] = {}
for i in range(len(lines)):
    if len(lines[i].strip()) <= 0:
        lines = lines[i + 1 :]
        break

    conn = list(map(int, lines[i].strip().split("|")))
    pages.setdefault(conn[0], set()).add(conn[1])


total = 0
for line in lines:
    order = list(map(int, line.strip().split(",")))

    correct = True
    for i in range(len(order) - 1):
        for j in range(i + 1, len(order)):
            u, v = order[i], order[j]
            if v in pages and u in pages[v]:
                correct = False
                break
        if not correct:
            break

    if correct:
        continue

    for start in range(int(len(order) / 2) + 1):
        find = -1
        for i in range(start, len(order)):
            every = True
            for j in range(start, len(order)):
                u, v = order[i], order[j]
                if u == v:
                    continue
                if v in pages and u in pages[v]:
                    every = False
                    break
            if every:
                find = i
                break

        swap = order[start]
        order[start] = order[find]
        order[find] = swap

    total += order[int(len(order) / 2)]

print(total)
