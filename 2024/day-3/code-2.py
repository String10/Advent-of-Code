import re

with open("puzzle.txt") as f:
    data = f.read()

r = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")

n = len(data)

total, start = 0, 0
enabled = True
while start < n:
    m = r.search(data, start)
    if m:
        if m.group() == "do()":
            enabled = True
        elif m.group() == "don't()":
            enabled = False
        elif enabled:
            a, b = map(int, m.groups())
            total += a * b
        start = m.end()
    else:
        break

print(total)
