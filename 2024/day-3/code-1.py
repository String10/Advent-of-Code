import re

with open("puzzle.txt") as f:
    data = f.read()

r = re.compile(r"mul\((\d+),(\d+)\)")

n = len(data)

total, start = 0, 0
while start < n:
    m = r.search(data, start)
    if m:
        a, b = map(int, m.groups())
        total += a * b
        start = m.end()
    else:
        break

print(total)
