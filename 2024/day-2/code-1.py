with open("puzzle.txt") as f:
    data = f.read().splitlines()

data = [[int(num) for num in x.split(" ")] for x in data]

total = 0

for row in data:
    if all(
        [
            row[i] - row[i + 1] >= 1 and row[i] - row[i + 1] <= 3
            for i in range(len(row) - 1)
        ]
    ) or all(
        [
            row[i + 1] - row[i] >= 1 and row[i + 1] - row[i] <= 3
            for i in range(len(row) - 1)
        ]
    ):
        total += 1

print(total)
