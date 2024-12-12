with open("puzzle.txt") as f:
    data = f.read().splitlines()

data = [[int(num) for num in x.split(" ")] for x in data]

total = 0

for row in data:
    num = len(row)

    if num <= 3:
        total += 1
        continue

    def check(start, end, direction=1, skip=None):
        for i in range(start, end):
            if skip is not None:
                if i == skip:
                    continue
                if i + 1 == skip:
                    if i + 2 < num and not (
                        direction * (row[i] - row[i + 2]) >= 1
                        and direction * (row[i] - row[i + 2]) <= 3
                    ):
                        return False
                    continue

            if (
                direction * (row[i] - row[i + 1]) >= 1
                and direction * (row[i] - row[i + 1]) <= 3
            ):
                continue
            return False
        return True

    if (
        check(0, num - 1)
        or check(0, num - 1, -1)
        or check(1, num - 1)
        or check(1, num - 1, -1)
        or check(0, num - 2)
        or check(0, num - 2, -1)
    ):
        total += 1
        continue

    if row[0] < row[num - 1]:
        direction = -1
    elif row[0] > row[num - 1]:
        direction = 1
    else:
        continue

    error = 0
    for i in range(num - 1):
        if (
            direction * (row[i] - row[i + 1]) < 1
            or direction * (row[i] - row[i + 1]) > 3
        ):
            error = i
            break

    total += (
        1
        if check(0, num - 1, direction, error)
        or check(0, num - 1, direction, error + 1)
        else 0
    )

print(total)
